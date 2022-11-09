#
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.utils.html import format_html
#
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, 'base/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'base/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    # if topic.owner != request.user:
    #     raise Http404
    list_display = ['content', ]
    def get_content(self, obj):
        format_html(obj)
    

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'base/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = TopicForm()
    else:
    # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('base:topics'))
    context = {'form': form}
    return render(request, 'base/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = EntryForm()
    else:
    # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('base:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'base/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
    # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
    # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'base/edit_entry.html', context)

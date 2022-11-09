from email.policy import default
from io import open_code
from pyexpat import model

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Topic(models.Model):

    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    content= RichTextField(null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):

        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):

    """Something specific learned about a topic"""
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        default= None
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default= None
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default= True)
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):

        """Return a string representation of the model."""
        return self.text[:50] + "..."

# class ItemBased(models.Model):
#     class Meta:
#         abstract= True
#     subject = models.CharField(max_length=255 )
#     created_date= models.DateTimeField(auto_now_add= True)
#     updated_date= models.DateTimeField(auto_now=True)
#     active= models.BooleanField(default= True)
    
#     def __str__(self):
#         return self.subject


# class Lession(ItemBased):
#     class Meta:
#             unique_together= ('subject', 'course')
#     image= models.ImageField(upload_to= 'static/images/%Y/%m', default= None)
#     course= models.ForeignKey(
#             Topic,
#             on_delete= models.CASCADE
#             )
#     tags= models.ManyToManyField('Tag', blank=True, null= True)   

# class Tag(models.Model):
#     name= models.CharField(max_length= 50, unique= True)

#     def __str__(self):
#         return self.name


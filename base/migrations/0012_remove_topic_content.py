# Generated by Django 4.1.2 on 2022-11-02 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_topic_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='content',
        ),
    ]

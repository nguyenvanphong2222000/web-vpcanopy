# Generated by Django 4.1.2 on 2022-11-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_tag_lession_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
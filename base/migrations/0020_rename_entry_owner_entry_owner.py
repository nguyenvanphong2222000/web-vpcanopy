# Generated by Django 4.1.2 on 2022-11-09 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_entry_entry_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry_owner',
            new_name='owner',
        ),
    ]

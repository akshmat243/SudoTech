# Generated by Django 5.2 on 2025-05-05 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OneNoteNotebook',
            new_name='Notebook',
        ),
    ]

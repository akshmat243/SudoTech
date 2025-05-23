# Generated by Django 5.2 on 2025-05-03 07:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZulipMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(help_text='Zulip message ID', max_length=100, unique=True)),
                ('sender_email', models.EmailField(help_text='Email of the message sender', max_length=254)),
                ('recipient', models.CharField(help_text='Stream name or recipient email', max_length=255)),
                ('topic', models.CharField(blank=True, help_text='Topic for stream messages', max_length=255)),
                ('message_type', models.CharField(choices=[('stream', 'Stream'), ('private', 'Private')], max_length=20)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

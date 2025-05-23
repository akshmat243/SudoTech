# Generated by Django 5.2 on 2025-05-03 07:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='YouTubePlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='youtube.youtubechannel')),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('published_at', models.DateTimeField()),
                ('url', models.URLField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='youtube.youtubechannel')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='youtube.youtubeplaylist')),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('upload', 'Upload'), ('like', 'Like'), ('comment', 'Comment'), ('subscribe', 'Subscribe'), ('share', 'Share')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('occurred_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.youtubechannel')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtube.youtubevideo')),
            ],
        ),
    ]

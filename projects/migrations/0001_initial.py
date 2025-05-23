# Generated by Django 5.2 on 2025-05-04 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stage', models.CharField(choices=[('ongoing', 'Ongoing'), ('onhold', 'OnHold'), ('finished', 'Finished')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('progress', models.PositiveIntegerField(help_text='Enter progress as a percentage (0–100)')),
                ('stage', models.CharField(choices=[('ongoing', 'Ongoing'), ('onhold', 'OnHold'), ('finished', 'Finished')], max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

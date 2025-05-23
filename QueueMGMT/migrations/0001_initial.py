# Generated by Django 5.2 on 2025-05-04 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_tokens', models.PositiveIntegerField()),
                ('tokens_served', models.PositiveIntegerField()),
                ('tokens_missed', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QueueMGMT.service')),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_open', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='QueueMGMT.service')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_number', models.PositiveIntegerField()),
                ('called_at', models.DateTimeField(auto_now_add=True)),
                ('served', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('counter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QueueMGMT.counter')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QueueMGMT.service')),
            ],
        ),
    ]

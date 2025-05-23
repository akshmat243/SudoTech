# Generated by Django 5.2 on 2025-05-04 05:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('support_email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cleaning.cleaningteam')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_text', models.TextField()),
                ('date_submitted', models.DateField(default=django.utils.timezone.now)),
                ('resolved', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cleaning.bookingrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector_name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('inspection_date', models.DateField(default=django.utils.timezone.now)),
                ('passed', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cleaning.bookingrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_issued', models.DateField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cleaning.bookingrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('date_reported', models.DateField(default=django.utils.timezone.now)),
                ('resolved', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cleaning.cleaningteam')),
            ],
        ),
    ]

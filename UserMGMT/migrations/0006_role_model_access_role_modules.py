# Generated by Django 5.2 on 2025-05-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserMGMT', '0005_role_permission_delete_rolemodelpermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='model_access',
            field=models.ManyToManyField(blank=True, to='UserMGMT.modelaccess'),
        ),
        migrations.AddField(
            model_name='role',
            name='modules',
            field=models.ManyToManyField(blank=True, to='UserMGMT.module'),
        ),
    ]

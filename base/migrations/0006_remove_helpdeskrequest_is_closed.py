# Generated by Django 5.0.4 on 2024-04-20 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_helpdeskrequest_decline_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpdeskrequest',
            name='is_closed',
        ),
    ]

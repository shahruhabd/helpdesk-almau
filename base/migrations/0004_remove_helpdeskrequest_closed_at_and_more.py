# Generated by Django 5.0.4 on 2024-04-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_helpdeskrequest_conversation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpdeskrequest',
            name='closed_at',
        ),
        migrations.AddField(
            model_name='helpdeskrequest',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='Закрыта'),
        ),
    ]

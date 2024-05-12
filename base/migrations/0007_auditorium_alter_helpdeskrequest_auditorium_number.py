# Generated by Django 5.0.4 on 2024-05-08 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_helpdeskrequest_is_closed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='Номер аудитории')),
            ],
        ),
        migrations.AlterField(
            model_name='helpdeskrequest',
            name='auditorium_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.auditorium', verbose_name='Аудитория'),
        ),
    ]
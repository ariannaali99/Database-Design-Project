# Generated by Django 4.1.2 on 2022-10-21 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='displayname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

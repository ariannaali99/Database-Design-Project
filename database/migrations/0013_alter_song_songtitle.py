# Generated by Django 4.1.2 on 2022-11-22 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_alter_song_songid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='songTitle',
            field=models.CharField(max_length=30),
        ),
    ]
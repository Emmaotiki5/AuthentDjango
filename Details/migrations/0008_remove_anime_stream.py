# Generated by Django 4.2.3 on 2023-07-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0007_remove_anime_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='stream',
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0005_remove_anime_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='img',
            field=models.CharField(default='Hello', max_length=100),
            preserve_default=False,
        ),
    ]
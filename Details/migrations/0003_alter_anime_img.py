# Generated by Django 4.2.3 on 2023-07-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0002_anime_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='img',
            field=models.ImageField(upload_to='{% static "img" %}'),
        ),
    ]
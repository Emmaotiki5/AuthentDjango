# Generated by Django 4.2.3 on 2023-07-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Details', '0009_delete_anime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField(max_length=500)),
                ('anime_id', models.CharField(max_length=100)),
            ],
        ),
    ]

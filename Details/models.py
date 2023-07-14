from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    anime_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class DownloadLink(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='download_links')
    link = models.URLField(max_length=500)
    episode_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.anime.title} - Episode {self.episode_number}"

import requests
from bs4 import BeautifulSoup
from gogoanime import get_anime_recent, get_anime_details
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authentication.settings")
import django
django.setup()
from Details.models import Anime, DownloadLink


def purge_data():
    # Delete all objects in the DownloadLink model
    DownloadLink.objects.all().delete()


    # Delete all objects in the Anime model
    Anime.objects.all().delete()
purge_data()
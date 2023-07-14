import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authentication.settings')

# Initialize the Django application
django.setup()

# Import the necessary models
from Details.models import Anime
from gogoanime import get_anime_recent, get_anime_details

def bulkimport():
    recent_anime = get_anime_recent(type=1, page=1)

    for anime in recent_anime:
        title = anime['title']
        image_url = anime['image']
        anime_id = anime['id']

        try:
            details = get_anime_details(id=anime_id)
            
            description = ''
            for detail in details:
                if 'description' in detail:
                    description = detail['description']
                    break
            
            anime_obj = Anime(title=title, description=description, image_url=image_url, anime_id=anime_id)
            anime_obj.save()
            print("Successful:", title)
        
        except AttributeError:
            anime_obj = Anime(title=title, description='No description', image_url=image_url, anime_id=anime_id)
            anime_obj.save()
            print("Successful (No Description):", title)

bulkimport()

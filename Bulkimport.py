import requests
from bs4 import BeautifulSoup
from gogoanime import get_anime_recent, get_anime_details
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authentication.settings")
import django
django.setup()
from Details.models import Anime, DownloadLink


def find_download_links(anime_id):
    base_url = "https://gogoanimehd.to"
    episode = 0
    download_links = {}

    while True:
        episode += 1
        link = f"{base_url}/{anime_id}-episode-{episode}"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link_tags = soup.find_all('a')

        if not download_link_tags:
            break

        download_link_found = False
        for download_link_tag in download_link_tags:
            url = download_link_tag.get('href', 'No URL available')
            if "https://gotaku1.com/download" in url:
                modified_url = url.replace("Gogoanime", "")
                download_links[episode] = modified_url
                print(f"Download link found for Episode {episode}: {modified_url}")
                download_link_found = True
                break

        if not download_link_found:
            break

    return download_links




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
            
            # Check if the anime with the same anime_id already exists
            anime_obj, created = Anime.objects.get_or_create(anime_id=anime_id, defaults={
                'title': title,
                'description': description,
                'image_url': image_url,
            })

            if created:
                print(f"Created Anime object for: {title}")
            else:
                print(f"Anime object already exists for: {title}")

            # Find the download links
            download_links = find_download_links(anime_id)

            # Update the anime object with the download links
            for episode_number, download_link in download_links.items():
                # Check if the DownloadLink with the same episode_number and anime_id already exists
                download_obj, created = DownloadLink.objects.get_or_create(anime=anime_obj, episode_number=episode_number, defaults={
                    'link': download_link,
                })

                if created:
                    print(f"Download link saved for Episode {episode_number}")
                else:
                    print(f"Download link already exists for Episode {episode_number}")

            # Handle animes starting from episode 0
            if 0 in download_links:
                # Check if the DownloadLink with episode_number=0 and anime_id already exists
                download_obj, created = DownloadLink.objects.get_or_create(anime=anime_obj, episode_number=0, defaults={
                    'link': download_links[0],
                })

                if created:
                    print("Download link saved for Episode 0")
                else:
                    print("Download link already exists for Episode 0")
        
        except AttributeError:
            # Handle the case where details are not found
            anime_obj, created = Anime.objects.get_or_create(anime_id=anime_id, defaults={
                'title': title,
                'description': 'No description',
                'image_url': image_url,
            })

            if created:
                print(f"Created Anime object for: {title}")
            else:
                print(f"Anime object already exists for: {title}")

            # Find the download links
            download_links = find_download_links(anime_id)

            # Update the anime object with the download links
            for episode_number, download_link in download_links.items():
                # Check if the DownloadLink with the same episode_number and anime_id already exists
                download_obj, created = DownloadLink.objects.get_or_create(anime=anime_obj, episode_number=episode_number, defaults={
                    'link': download_link,
                })

                if created:
                    print(f"Download link saved for Episode {episode_number}")
                else:
                    print(f"Download link already exists for Episode {episode_number}")

            # Handle animes starting from episode 0
            if 0 in download_links:
                # Check if the DownloadLink with episode_number=0 and anime_id already exists
                download_obj, created = DownloadLink.objects.get_or_create(anime=anime_obj, episode_number=0, defaults={
                    'link': download_links[0],
                })

                if created:
                    print("Download link saved for Episode 0")
                else:
                    print("Download link already exists for Episode 0")



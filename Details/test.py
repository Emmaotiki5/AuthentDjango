import gogo_scraper as gs
from bs4 import BeautifulSoup
import requests
from gogoanime import get_search_results, get_anime_details, get_anime_episode, get_anime_popular, get_anime_newseason, get_anime_recent  # type: ignore

def main(anime_id, anime_episode):
    gs.BASE_URL = "https://gogoanimehd.to"
    link = gs.getEpisode(anime_id, anime_episode)
    r = requests.get(link)
    s= r.text
    soup = BeautifulSoup(s, 'html.parser')
    links = soup.find_all('a')


    for link in links:
        url = link.get('href', 'No URL available')
        if "https://gotaku1.com/download" in url:
            kain = url
            modified_url = kain.replace("Gogoanime", "")
            print(modified_url)
            return modified_url
        else:
            pass
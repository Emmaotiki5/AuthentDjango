from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth # type: ignore
from django.http import HttpResponse
from django.contrib import messages
from .models import Anime
from gogoanime import get_search_results, get_anime_details, get_anime_episode, get_anime_popular, get_anime_newseason, get_anime_recent  # type: ignore
from django.core.paginator import Paginator
from .API import Kimi as api
import gogo_scraper as gs
from bs4 import BeautifulSoup
import requests

class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cache-Control'] = 'max-age=900'  # Set cache control for 15 minutes
        return response





# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email = email):
                messages.info(request, "There is an acount with this email already")
                return redirect('/register')
            elif User.objects.filter(username=username):
                messages.info(request, "This username is already in use")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password2,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('/register')
    else:                       
        return render(request, 'register.html')

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/anime')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('/login')
        else:
            return render(request, 'login.html')

def anime(request):
    animes = Anime.objects.all()
    titles = [anime.title for anime in animes]
    search_results = {}
    id_results = {}

    for title in titles:
        anime_episodes = get_search_results(query=title, page=1)
        for episode in anime_episodes:
            link = episode.get('image')  # Retrieve the image link
            ids = episode.get('id')
            episode['image_link'] = link  # Add the image link to the episode dictionary
            episode['id'] = ids
        search_results[title] = anime_episodes
        id_results[title] = [episode['id'] for episode in anime_episodes]

    return render(request, 'anime.html', {'animes': animes, 'search_results': search_results, 'id_results': id_results})








def logout(request):
    auth.logout(request)
    return redirect('/')

def find_download_link(anime_id, anime_episode):
    gs.BASE_URL = "https://gogoanimehd.to"
    link = gs.getEpisode(anime_id, anime_episode)
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        url = link.get('href', 'No URL available')
        if "https://gotaku1.com/download" in url:
            modified_url = url.replace("Gogoanime", "")
            return modified_url

    return None

def anime_details(request, pk):
    anime_details_list = get_anime_details(id=pk)
    describe = anime_details_list[0].get('description') if anime_details_list else None
    picture = anime_details_list[0].get('image') if anime_details_list else None

    episode_number = 1
    episode_list = []
    download_link = find_download_link(pk, episode_number)
    while download_link is not None:
        episode_list.append(episode_number)
        episode_number += 1
        download_link = find_download_link(pk, episode_number)

    context = {
        'pk': pk,
        'describe': describe,
        'picture': picture,
        'episode_list': episode_list
    }

    return render(request, 'stream.html', context)



index = CacheMiddleware(index)
register = CacheMiddleware(register)
login = CacheMiddleware(login)
anime = CacheMiddleware(anime)
logout = CacheMiddleware(logout)
anime_details = CacheMiddleware(anime_details)



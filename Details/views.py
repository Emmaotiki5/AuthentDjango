from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth # type: ignore
from django.contrib import messages
from .models import Anime, DownloadLink
from gogoanime import get_search_results, get_anime_details, get_anime_recent  # type: ignore
import gogo_scraper as gs
from bs4 import BeautifulSoup
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponseNotFound










# Create your views here.
@cache_page(60 * 15)  # Cache the page for 15 minutes (900 seconds)
def index(request):
    return render(request, 'index.html')
@cache_page(60 * 15)  # Cache the page for 15 minutes (900 seconds)
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
@cache_page(60 * 15)  # Cache the page for 15 minutes (900 seconds)
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
@cache_page(60 * 15)  # Cache the page for 15 minutes (900 seconds)
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


@cache_page(60 * 15)  # Cache the page for 15 minutes (900 seconds)
def anime_details(request, anime_id):
    anime = Anime.objects.get(anime_id=anime_id)
    describe = anime.description
    picture = anime.image_url
    episode_download_list = anime.download_links.all().values_list('episode_number', 'link')

    context = {
        'anime_id': anime.anime_id,
        'describe': describe,
        'picture': picture,
        'episode_download_list': episode_download_list
    }

    return render(request, 'stream.html', context)

   





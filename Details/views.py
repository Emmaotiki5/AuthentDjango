from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Anime
from gogoanime import get_search_results, get_anime_details, get_anime_episode, get_anime_popular, get_anime_newseason, get_anime_recent
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

    for title in titles:
        anime_episode = get_search_results(query=title, page=1)
        search_results[title] = anime_episode

    return render(request, 'anime.html', {'animes': animes, 'search_results': search_results})




def logout(request):
    auth.logout(request)
    return redirect('/')





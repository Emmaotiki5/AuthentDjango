from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('anime', views.anime, name='anime'),
    path ('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

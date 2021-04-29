from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('faq', views.faq, name='faq'),
    path('UnderTea', views.sergey, name='sergey'),
    path('Maxim', views.max, name='max'),
    path('Denis', views.den, name='den'),
    path('Donate', views.don, name='don'),
    path('login', views.login, name='login'),
    path('titrs', views.titrs, name='titrs'),

# sergey-branding
    path('portfolio', views.portfolio, name='portfolio'),
    path('paper', views.paper, name='paper'),
    path('GameLibrary', views.GameLibrary, name='GameLibrary'),
    path('anime-is-shit', views.anime, name='anime'),
    path('word', views.word, name='wordiswater'),

# login
    path('register', views.register, name='register'),
]
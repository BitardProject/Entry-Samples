from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def faq(request):
    return render(request, 'main/faq.html')


def sergey(request):
    return render(request, 'main/sergey.html')


def max(request):
    return render(request, 'main/max.html')


def den(request):
    return render(request, 'main/den.html')


def don(request):
    return render(request, 'main/don.html')


def login(request):
    return render(request, 'main/login.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def register(request):
    return render(request, 'main/register.html')


def titrs(request):
    return render(request, 'main/titrs.html')


def paper(request):
    return render(request, 'main/paper.html')


def GameLibrary(request):
    return render(request, 'main/GameLibrary.html')


def anime(request):
    return render(request, 'main/anime.html')


def word(request):
    return render(request, 'main/word.html')
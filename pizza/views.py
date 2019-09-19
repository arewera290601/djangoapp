from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Witaj w barze Dżungla!!")
    return render(request, 'pizza/index.html')

def news(request):
    return HttpResponse("<h1>Nowości w dżungli!</h1>")

def gallery(request):
    return HttpResponse("<h2>Galeria zdjęć!</h2>")

def kontakt(request):
    return HttpResponse("<h2>Kontakt z dżunglą!</h2>")

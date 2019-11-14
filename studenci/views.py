from django.shortcuts import render, redirect
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia
from django.contrib import messages
from studenci.form import StudentLoginForm
from studenci.form import UczelniaForm, MiastoForm
from django.urls import reverse

def index(request):
    #return HttpResponse("Witaj w aplikacji Studenci!")
    return render(request, 'studenci/index.html')


def news(request):
    #return HttpResponse("<h1>Nowości u studentów</h1>")
    return render(request, 'pizza/news.html')

def miasta(request):

    if request.method == 'POST':
        #nazwa= request.POST.get('nazwa')
        #kod= request.POST.get('kod')
        form = MiastoForm(request.POST)
        if form.is_valid():
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane deb***!")
    else:
        form = MiastoForm()

    miasta = Miasto.objects.all()
    kontekst = {
        'form': form,
        'miasta': miasta
    }
    return render(request, 'studenci/miasta.html', kontekst)


def uczelnia(request):

    if request.method == 'POST':
        form = UczelniaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Dane zapisano!")
            # przekierowanie
            return redirect(reverse('studenci:uczelnia'))
    else:
        form = UczelniaForm()

    uczelnia = Uczelnia.objects.all()
    kontekst = {
        'form': form,
        'uczelnia': uczelnia
    }

    return render(request, 'studenci/uczelnia.html', kontekst)

def login(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        kod= request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane!")
    else:
        form = StudentLoginForm()


    kontekst = { 'form': form }
    return render(request, 'studenci/login.html', kontekst)

def login2(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        kod= request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane!")
    else:
        form = UczelniaForm()


    kontekst = { 'form': form }
    return render(request, 'studenci/login2.html', kontekst)

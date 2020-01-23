from django.urls import path
from django.views.generic import ListView
from . import views
from studenci.models import Miasto

app_name = 'studenci'
urlpatterns = [
	path('', views.index, name='index'),
    path('miasta/lista', ListView.as_view(model=Miasto), name='miasta_lista'),
    path('news/', views.news, name='news'),
    path('miasta/', views.miasta, name='miasta'),
    path('miasta/dodaj', views.DodajMiasto.as_view(), name='miasta_dodaj'),
    path('miasta/edytuj/<int:pk>', views.EdytujMiasto.as_view(), name='miasta_edytuj'),
    path('miasta/usun/<int:pk>', views.UsunMiasto.as_view(), name='miasta_usun'),
    path('uczelnia/', views.uczelnia, name='uczelnia'),
    path('uczelnia/lista', views.ListaUczelni.as_view(), name='uczelnie_lista'),
    path('uczelnia/dodaj', views.DodajUczelnia.as_view(), name='uczelnia_dodaj'),
    path('login/', views.login, name='login'),
    path('login2/', views.login2, name='login2'),

]

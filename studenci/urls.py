from django.urls import path

from . import views

app_name = 'studenci'
urlpatterns = [
	path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('miasta/', views.miasta, name='miasta'),
    path('uczelnia/', views.uczelnia, name='uczelnia'),
    path('login/', views.login, name='login'),
    path('login2/', views.login2, name='login2'),

]

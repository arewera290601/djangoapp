from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('miasta/', views.miasta, name='miasta'),
    path('uczelnia/', views.uczelnia, name='uczelnia'),

]

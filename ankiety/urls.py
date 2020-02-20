from django.urls import path
from . import views

app_name = 'ankiety'
urlpatterns = [
	path('', views.ListaPytan.as_view(), name='lista-pytan'),

]

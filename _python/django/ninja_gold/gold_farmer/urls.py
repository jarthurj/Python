from django.urls import path
from . import views

urlpatterns =[
	path('', views.index),
	path('get_gold_farm/', views.get_gold_farm),
	path('get_gold_cave/', views.get_gold_cave),
	path('get_gold_house/', views.get_gold_house),
	path('get_gold_casino/', views.get_gold_casino),
]
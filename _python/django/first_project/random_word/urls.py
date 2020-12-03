from django.urls import path
from . import views

urlpatterns = [
	path('random_word_index/', views.index),
	path('random_word/', views.random_word),
	path('random_word/get_word/', views.get_word),
	path('get_word/', views.get_word),
	path('reset/', views.index),
	
]
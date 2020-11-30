from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('new/', views.new),
	path('create/', views.create),
	path('<int:num>', views.blognumber),
	path('<int:num>/edit', views.edit),
	path('<int:num>/delete', views.destroy)
]
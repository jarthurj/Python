from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('shows', views.shows),
	path('shows/<int:show_id>', views.show_info),
	path('shows/new', views.new_show),
	path('add_show/', views.add_show),
	path('shows/<int:show_id>/edit', views.edit_show),
	path('edit_show/', views.make_updates),
	path('shows/<int:show_id>/destroy', views.delete),
]


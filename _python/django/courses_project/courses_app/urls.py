from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('add_course', views.add_course),
	path('delete/<int:course_id>', views.delete_course),
	path('comments/<int:course_id>', views.comments),
	path('confirm_delete/<int:course_id>', views.confirm_delete),
	path('add_comment/<int:course_id>', views.add_comment)
]

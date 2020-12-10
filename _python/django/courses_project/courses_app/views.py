from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages
def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'index.html',context)

def add_course(request):
	errors = None
	errors = Course.objects.basic_validator(request.POST)
	
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	course_name = request.POST['course_name']
	description = request.POST['description']
	new_course = Course.objects.create(course_name = course_name)
	Description.objects.create(description = description, course = new_course)
	return redirect('/')

def delete_course(request,course_id):
	if request.method == 'POST':
		course_to_delete = Course.objects.get(id=course_id)
		course_to_delete.delete()
		return redirect('/')
	else:
		return redirect(f'/confirm_delete/{course_id}')

def confirm_delete(request, course_id):
	context = {
		"course" : Course.objects.get(id=course_id)
	}
	return render(request, 'delete.html', context)


def add_comment(request, course_id):
	new_comment = Comment.objects.create(comment = request.POST['comment'], course = Course.objects.get(id=course_id))
	return redirect(f'/comments/{course_id}')
def comments(request, course_id):
	course = Course.objects.get(id=course_id)
	context ={
		"comments": course.comments.all,
		"course_id" : course_id
	}
	return render(request, 'comment.html', context)

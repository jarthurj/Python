from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse("placeholder to later display a list fo all blogs")

def new(request):
	return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
	return HttpResponseRedirect("/")

def blognumber(request, num):
	return HttpResponse("placeholder to display blog {}".format(num))

def edit(request, num):
	return HttpResponse("placeholder to edit.  blog {}".format(num))

def destroy(request, num):
	return HttpResponseRedirect("/")
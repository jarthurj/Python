from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
	return redirect('/shows')

def shows(request):
	context = {
		'shows': Show.objects.all()
	}
	return render(request, 'shows.html', context)

def show_info(request, show_id):
	show = None
	try:
		show = Show.objects.get(id=show_id)
	except:
		return redirect('/')
	context = {
		'show' :Show.objects.get(id=show_id)
	}
	return render(request, 'show.html', context)

def new_show(request):
	return render(request, 'new_show.html')

def add_show(request):
	errors = None
	errors = Show.objects.basic_validator(request.POST)
	
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/shows/new')
	else:
		title = request.POST['title']
		network = request.POST['network']
		release_date = request.POST['release_date']
		description = request.POST['description']
		Show.objects.create(title=title, network=network, release_date=release_date, description=description)
		show_url = f"/shows/{Show.objects.last().id}"
	return redirect(show_url)

def edit_show(request, show_id):
	show = Show.objects.get(id=show_id)
	release_date = show.release_date
	month = release_date.month
	day = release_date.day
	if month < 10:
		month = f"0{month}"
	if day < 10:
		day = f"0{day}"
	context = {
		'show':show,
		'date':f"{release_date.year}-{month}-{day}",
	}
	return render(request, 'edit.html', context)

def make_updates(request):
	errors = Show.objects.basic_validator(request.POST)
	show_id = request.POST['id']
	if len(errors) > 0:
		for key, value in errors.items():
			message.error(request, value)
		error_url = f'shows/{show_id}/edit'
		return redirect(error_url)
	else:
		show_to_update = Show.objects.get(id=request.POST['id'])
		if (request.POST['title'] != show_to_update.title or 
			request.POST['network'] != show_to_update.network or
			request.POST['release_date'] != show_to_update.release_date or
			request.POST['description'] != show_to_update.description):
			show_to_update.title = request.POST['title']
			show_to_update.network = request.POST['network']
			show_to_update.release_date = request.POST['release_date']
			show_to_update.description = request.POST['description']
			show_to_update.save()
			messages.success(request, "Show updated sucessfully")
	show_url = f"/shows/{show_to_update.id}"
	return redirect(show_url)

def delete(request, show_id):
	show = Show.objects.get(id=show_id)
	show.delete()
	return redirect('/')
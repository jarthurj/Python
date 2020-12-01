from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'index.html')

def result(request):
	if request.method == "POST":
		context={
			'name' : request.POST['your_name'],
			'language' : request.POST['language'],
			'location' : request.POST['location']}
		return render(request, 'output.html', context)

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	request.session['result'] = None
	return render(request, 'index.html')

# def result(request):
# 	if request.method == "POST":
# 		context={
# 			'name' : request.POST['your_name'],
# 			'language' : request.POST['language'],
# 			'location' : request.POST['location']}
# 		return render(request, 'output.html', context)
# 		return redirect('output.html')

def survey(request):
	if request.method == "POST":
		request.session['result'] = {
		'name' : request.POST['your_name'],
		'language': request.POST['language'],
		'location': request.POST['location']}
	else: 
		return redirect('/')
	return redirect('/result')

def result(request):
	context = {
		'result': request.session['result']
	}
	return render(request, 'output.html', context)
	

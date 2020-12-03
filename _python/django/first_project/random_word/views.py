from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
def index(request):
	request.session['attempts'] = 0
	context = {
		'random' :"press generate to get a random word"
	}
	return render(request, 'index.html', context)


def get_word(request):
	request.session['attempts'] += 1
	return redirect('/random_word/')

def random_word(request):
	random_word = get_random_string(length=14)
	context = {
		'random' :random_word
	}
	return render(request, 'random.html', context)

def reset(request):
	return redirect('/random_word_index/')
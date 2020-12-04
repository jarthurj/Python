from django.shortcuts import render
import random
def index(request):
	request.session['gold'] = 0
	request.session['log'] = ''
	return render(request, 'index.html')

def get_gold_farm(request):
	gold_found = random.randint(9,20)
	request.session['gold'] += gold_found
	request.session['log']+= f"\n You found {gold_found} at the farm"
	return render(request, 'index.html')

def get_gold_cave(request):
	gold_found = random.randint(4,10)
	request.session['gold'] += gold_found
	request.session['log']+= f"\n You found {gold_found} in the cave"
	return render(request, 'index.html')

def get_gold_house(request):

	gold_found = random.randint(1,5)
	request.session['gold'] += gold_found
	request.session['log']+= f"\n You found {gold_found} in a house"
	return render(request, 'index.html')

def get_gold_casino(request):
	gold_found = random.randint(-51,50)
	request.session['gold'] += gold_found
	if gold_found > 0:
		request.session['log']+= f"\n You gambled and won {gold_found}"
	elif gold_found == 0:
		request.session['log']+= f"\n You gambled and broke even"
	elif gold_found < 0:
		request.session['log']+= f"\n You gambled and lost {gold_found}"
	return render(request, 'index.html')


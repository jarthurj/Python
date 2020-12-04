from django.shortcuts import render, redirect
import random

gold_intervals={
	'farm':(10,20),
	'cave':(5,10),
	'house':(2,5),
	'casino':(0,50)
}
def index(request):
	if 'gold' not in request.session or 'log' not in request.session:
		request.session['gold'] = 0
		request.session['log'] = ''
	return render(request, 'index.html')


def process_gold(request):
	location_type = request.POST['building']
	gold_found = 0
	if location_type != 'casino':
		gold_found = random.randint(gold_intervals[location_type][0], gold_intervals[location_type][1])

	else:
		if random.randint(0,1) < 1:
			gold_found = random.randint(gold_intervals[location_type][0], gold_intervals[location_type][1]) * -1
		else:
			gold_found = random.randint(gold_intervals[location_type][0], gold_intervals[location_type][1])
	request.session['gold'] += gold_found
	location_type = location_type[0].upper() + location_type[1:]
	request.session['log'] =f'You found {gold_found} at the {location_type}\n' + request.session['log']
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')

# def get_gold_farm(request):
# 	gold_found = random.randint(9,20)
# 	request.session['gold'] += gold_found
# 	request.session['log']+= f"\n You found {gold_found} at the farm"
# 	return render(request, 'index.html')

# def get_gold_cave(request):
# 	gold_found = random.randint(4,10)
# 	request.session['gold'] += gold_found
# 	request.session['log']+= f"\n You found {gold_found} in the cave"
# 	return render(request, 'index.html')

# def get_gold_house(request):

# 	gold_found = random.randint(1,5)
# 	request.session['gold'] += gold_found
# 	request.session['log']+= f"\n You found {gold_found} in a house"
# 	return render(request, 'index.html')

# def get_gold_casino(request):
# 	gold_found = random.randint(-51,50)
# 	request.session['gold'] += gold_found
# 	if gold_found > 0:
# 		request.session['log']+= f"\n You gambled and won {gold_found}"
# 	elif gold_found == 0:
# 		request.session['log']+= f"\n You gambled and broke even"
# 	elif gold_found < 0:
# 		request.session['log']+= f"\n You gambled and lost {gold_found}"
# 	return render(request, 'index.html')


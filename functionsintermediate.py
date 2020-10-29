import random
def randInt(min=0, max=100):
	if(min > max):
		min, max = max, min
	num = round((random.random() * (max-min) + min))
	return num

print(randInt(-15, 5))

import random
randomlist = []
for i in range(0,10):
	n = random.randint(1,100)
	randomlist.append(n)

some_list = randomlist

for x in range(0, len(some_list), 1):
	minimum = some_list[x]
	index = 0
	for y in range(x, len(some_list), 1):
		if some_list[y] <= minimum:
			minimum = some_list[y]
			index = y
	some_list[x],some_list[index] = some_list[index], some_list[x]
	print(some_list)
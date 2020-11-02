
import random
randomlist = []
for i in range(0,10):
	n = random.randint(1,100)
	randomlist.append(n)

some_list = randomlist

for x in range(0, len(some_list), 1):
	minimum = some_list[x]
	if minimum > some_list[x]:
		for y in range(x, 0, -1):
			if some_list[x] <= some_list[y]:
				index = y
		some_list = some_list[0,index]+some_list[x]+some_list[index + 1,]


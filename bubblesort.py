some_list = [1,6,3,8,9,5,1,67,7,3,67,8,5,4]
not_sorted = True
while not_sorted:
	triggered = False
	for x in range(0, len(some_list) - 1, 1):
		low = some_list[x]
		high = some_list[x + 1]
		if low > high:
			triggered = True
			some_list[x], some_list[x + 1] = some_list[x + 1], some_list[x]
	if triggered == False:
		not_sorted = False
	print(some_list)
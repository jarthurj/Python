#biggiesize
# def biggiesize(lister):
# 	ret_list = []
# 	for x in range(0, len(lister), 1):
# 		if lister[x] > 0:
# 			ret_list.append('big')
# 		else:
# 			ret_list.append(lister[x])
# 	return ret_list

# print(biggiesize([-1, 3, 5, -5]))

#count positives
# def countpos(lister):
# 	count = 0
# 	ret_list = []

# 	for x in range(0, len(lister), 1):
# 		ret_list.append(lister[x])
# 		if lister[x] > 0:
# 			count += 1
# 	ret_list = ret_list[:-1]
# 	ret_list.append(count)

# 	return ret_list

# print(countpos([1,6,-4,-2,-7,-2]))

#sum total
# def sumtotal(lister):
# 	sum = 0 
# 	for x in lister:
# 		sum += x
# 	return sum

# print(sumtotal([1,2,3,4]))

#average

# def average(lister):
# 	sum = 0
# 	for x in lister:
# 		sum += x
# 	return sum/len(lister)
# print(average([1,2,3,4]))

#length 
# def length(lister):
# 	count = 0
# 	for x in lister:
# 		count += 1
# 	return count

# print(length([1,1,1,1]))

#minimum
# def minimum(lister):
# 	min = 0
# 	count = 0
# 	for x in lister:
# 		if x < min:
# 			min = x
# 		count += 1
# 	if count == 0:
# 		return False
# 	return min

# print(minimum([37,2,1,-9]))
# print(minimum([]))

#max
# def max(lister):
# 	max = 0
# 	count = 0
# 	for x in lister:
# 		if x > max:
# 			max = x
# 		count += 1
# 	if count == 0:
# 		return False
# 	return max

# print(max([37,2,1,-9]))
# print(max([]))

# ultimate

# def ultimate(lister):
# 	maximum = 0
# 	minimum = 0
# 	summ = 0
# 	count = 0
# 	for x in lister:
# 		if x > maximum:
# 			maximum = x
# 		if x < minimum:
# 			minimum = x
# 		summ += x
# 		count += 1
# 	if count == 0:
# 		return False
# 	return {'sumtotal':summ,'maximum':maximum,'minimum':minimum, 'average':summ/count,'length':count}

# print(ultimate([1,1,1,1]))

# #reverse
# def reverse_list(lister):
# 	half_len = int(len(lister)/2)
# 	for x in range(0, half_len, 1):
# 		lister[x], lister[len(lister) - 1 - x] = lister[len(lister) - 1 - x],lister[x]
# 	return lister
# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9, 5]))
# print(reverse_list([]))
# print(reverse_list([1]))
# print(reverse_list([1, 2]))
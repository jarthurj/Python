# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# students[0]["last_name"] = "Bryant"
# sports_directory['soccer'][0] = "Andres"
# z[0]['y'] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)

# def itDict(list_of_d):

# 	for d in list_of_d:
# 		for key in d:
# 			print(key, d[key], end = ' ')
# 		print('\n')

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# # itDict(students)

# def itDict2(key_name, some_list):
# 	for d in some_list:
# 		print(d[key_name])

# itDict2('first_name', students)
# itDict2('last_name', students)

def printInfo(some_dict):

	for key in some_dict:
		print(len(some_dict[key]), key)
		for x in some_dict[key]:
			print(x)
		print('\n')
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
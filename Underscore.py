class Underscore:
    def map(self, iterable, callback):
    	lisd = []
    	for x in iterable:
    		lisd.append(callback(x))
    	return lisd
    def find(self, iterable, callback):
    	for x in iterable:
    		if callback(x):
    			return x
    def filter(self, iterable, callback):
    	lisd = []
    	for x in iterable:
    		if callback(x):
    			lisd.append(x)
    	return lisd
    def reject(self, iterable, callback):
    	lisd = []
    	for x in iterable:
    		if not callback(x):
    			lisd.append(x)
    	return lisd
_ = Underscore() 


# print(_.map([1,2,3], lambda x: x*2))
# print(_.find([1,2,3,4,5,6], lambda x: x>4))
# print(_.filter([1,2,3,4,5,6], lambda x: x%2==0))
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0))


import product

class Store:
	def __init__(self, name):
		self.name = name
		self.products = []
	def add_product(self, new_product):
		self.products.append(new_product)
	def sell_product(self, id):
		for product in self.products:
			if product.id == id:
				self.products.remove(product)
	def inflation(self, percent_given):
		for product in self.products:
			product.update_price(percent_given, True)
	def set_clearance(self, category, percent_discount):
		for product in self.products:
			if product.category == category:
				product.update_price(percent_discount, False)
	def print_inventory(self):
		for product in self.products:
			product.print_info()


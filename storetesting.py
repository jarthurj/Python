from store import Store
from product import Product
import uuid

clothes_Store = Store("Kohls")
pants1 = Product("jeans",10, "pants")
pants2 = Product("shorts",18, "pants")
clothes_Store.add_product(pants1)
clothes_Store.add_product(pants2)
clothes_Store.print_inventory()
clothes_Store.set_clearance("pants", 10)
clothes_Store.print_inventory()
ident = pants1.id
clothes_Store.sell_product(ident)
clothes_Store.print_inventory()



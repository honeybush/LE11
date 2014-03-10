class Ingredient:
	def __init__(self):
		self.name = "ingredient"
		self.quantity = 5
		self.status = "available"
	def report(self):
		ingredient = {}
		ingredient['Name'] = self.name
		ingredient['Quantity'] = self.quantity
		ingredient['Status'] = self.status
		return ingredient
	def update(self, n):
		if self.quantity < n:
			self.status = "unavailable"
		else:
			self.status = "available"
	def buy(self):
		amount = self.quantity
		amount = amount + 5
		self.quantity = amount
	def getIngredient(self, n): #mali ito
		self.update(n)
		amount = self.quantity
		cooked = 0
		if self.status == "available":
			amount = amount - n
			self.quantity = amount
			cooked = 3
		else:
			cooked = 0
		return cooked
class Beef(Ingredient):
	def __init__(self):
		self.name = "beef"
		self.quantity = 5
		self.status = "available"
class Pasta(Ingredient):
	def __init__(self):
		self.name = "pasta"
		self.quantity = 5
		self.status = "available"
class Cheese(Ingredient):
	def __init__(self):
		self.name = "cheese"
		self.quantity = 5
		self.status = "available"
class Tomato(Ingredient):
	def __init__(self):
		self.name = "tomato"
		self.quantity = 5
		self.status = "available"
class Leaves(Ingredient):
	def __init__(self):
		self.name = "leaves"
		self.quantity = 5
		self.status = "available"
class Banana(Ingredient):
	def __init__(self):
		self.name = "banana"
		self.quantity = 5
		self.status = "available"
class Cream(Ingredient):
	def __init__(self):
		self.name = "cream"
		self.quantity = 5
		self.status = "available"
class IceCream(Ingredient):
	def __init__(self):
		self.name = "ice cream"
		self.quantity = 5
		self.status = "available"
class Chocolate(Ingredient):
	def __init__(self):
		self.name = "chocolate"
		self.quantity = 5
		self.status = "available"
class Milk(Ingredient):
	def __init__(self):
		self.name = "milk"
		self.quantity = 5
		self.status = "available"
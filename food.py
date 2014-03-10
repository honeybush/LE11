class Food:
	def __init__(self):
		self.name = "food"
		self.cooked = 0
		self.ingredients = {}
	def report(self):
		food = {}
		food['Name'] = self.name
		food['Quantity'] = self.cooked
		return food
class Lasagna(Food):
	def __init__(self):
		self.name = "lasagna"
		self.cooked = 0
		self.ingredients = {"beef": 2, "pasta": 1, "cheese": 1, "tomato": 1}
class VegPlatter(Food):
	def __init__(self):
		self.name = "vegetarian platter"
		self.cooked = 0
		self.ingredients = {"leaves": 1, "cheese": 1, "tomato": 1}
class BananaSplit(Food):
	def __init__(self):
		self.name = "banana split"
		self.cooked = 0
		self.ingredients = {"banana": 1, "cream": 1, "ice cream": 3}
class Sundae(Food):
	def __init__(self):
		self.name = "sundae"
		self.cooked = 0
		self.ingredients = {"chocolate": 2, "cream": 1, "ice cream": 2}
class BubbleTea(Food):
	def __init__(self):
		self.name = "bubble tea"
		self.cooked = 0
		self.ingredients = {"leaves": 2, "cream": 1}
class ChocoMilkshake(Food):
	def __init__(self):
		self.name = "chocolate milkshake"
		self.cooked = 0
		self.ingredients = {"chocolate": 3, "ice cream": 1, "cream": 1}

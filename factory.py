class Ingredient:
	def __init__(self):
		self.name = ""
		self.amount = 0

class Food:
	def __init__(self):
		self.name = ""
		self.ingredients = {}
		self.timeCooked = 0.0
	def timer(self):
		t = Timer(self.timeCooked, self.cooking)
	def cooking(self):
		print "-"

class Factory:
	def __init__(self, _type):
		if _type = "ing":
			self.make_ing()
		else:
			self.make_food()
	def make_ing(self):
		self.ingredients = {}
		open_ing(self.ingredients)
	def make_food(self):
        self.finished = {}
        open_fin(self.finished)
	def open_ing(ing):
		file = open('ing.txt', 'r')
		for x in file:
			x = x.split("=")
			ing[x[0].strip()] = int(x[1].strip())
		file.close()
	def open_fin(fin):
		file = open('fin.txt', 'r')
		for x in file:
			fin[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
		file.close()
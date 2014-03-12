class Ingredient:
	def __init__(self):
		self.name = ""
		self.type = ""

class Food:
	def __init__(self):
		self.name = ""
		self.ingredients = {}
		self.timeCooked = 0

class Factory:
	def __init__(self, _type):
		if _type = "ing":
			self.make_ing()
		else:
			self.make_food()
	def make_ing(self):
		print "-"
	def make_food(self):
		print "-"
	def open_fin(fin):
		file = open('fin.txt', 'r')
		for x in file:
			fin[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
		file.close()
	def open_recipe():
		rec_list = []
		file = open("Recipe.txt","r")
		for x in file:
			try:
				if "\t" not in x:
					rec_list.append(temp)
					temp = Food()
					temp.name = x.split(':')[0].strip()
					temp.kind = x.split(':')[1].strip()
				else:
					temp.ing[x.split(":")[0].strip()]= int(x.split(":")[1].strip())
			except UnboundLocalError:
				temp = Food()
				temp.name = x.split(':')[0].strip()
				temp.kind = x.split(':')[1].strip()
		rec_list.append(temp)
		return rec_list
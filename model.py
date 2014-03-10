from Tkinter import*

class Data:
	def __init__(self):
		self.inglist = {"beef":0, "pasta":0, "cheese":0, "tomato":0, "leaves":0, "banana":0, "cream":0, "icecream":0, "chocolate":0}
		self.foodlist = {"lasagna":0, "vegplatter":0, "bananasplit":0, "sundae":0, "bbt":0, "chocomilkshake":0}
		self.beef = 0
		self.pasta = 0
		self.cheese = 0
		self.tomato = 0
		self.leaves = 0
		self.banana = 0
		self.cream = 0
		self.icecream = 0
		self.chocolate = 0
		self.lasagna= 0
		self.vegplatter = 0
		self.bananasplit = 0
		self.sundae = 0
		self.bbt = 0
		self.chocomilkshake = 0
		self.init_ing()
	def addIng(self, ing, n):
		self.inglist[ing] = self.inglist(ing) + n
		self.set_int()
	def redIng(self, ing, n):
		self.inglist[ing] = self.inglist(ing) - n
		self.set_int()
	def addFood(self, food):
		self.foodlist[food] = self.foodlist(food) - 3
		self.set_food()
	def redFood(self, food, n):
		self.foodlist[food] = self.foodlist(food) - n
		self.set_food()
	def init_ing(self):
		f = open("ing.txt", "r")
		s = []
		a = ""
		for line in f:
			a = line
			a = a.split(" ")
			s.append(a)
		for i in s:
			i[2] = i[2].rstrip("\n")
			self.inglist[i[0]] = i[2]
		f.close
		self.set_ing()
	def set_food(self):
		self.lasagna = self.foodlist.get("lasagna", 0)
		self.vegplatter = self.foodlist.get("vegplatter", 0)
		self.bananasplit = self.foodlist.get("bananasplit", 0)
		self.sundae = self.foodlist.get("sundae", 0)
		self.bbt = self.foodlist.get("bbt", 0)
		self.chocomilkshake = self.foodlist.get("chocomilkshake", 0)
	def set_ing(self):
		self.beef = self.inglist.get("beef", 0)
		self.pasta = self.inglist.get("pasta", 0)
		self.cheese = self.inglist.get("cheese", 0)
		self.tomato = self.inglist.get("tomato", 0)
		self.leaves = self.inglist.get("leaves", 0)
		self.banana = self.inglist.get("banana", 0)
		self.cream = self.inglist.get("cream", 0)
		self.icecream = self.inglist.get("icecream", 0)
		self.chocolate = self.inglist.get("chocolate", 0)

model = Data()
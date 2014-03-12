from Tkinter import*
import model

class CC:
	def __init__(self):
		self.ing_list = []
		self.food_list = []
		self.order_f = {}
		self.order_i = {}
		self.cookOrder = {}
		self.data = model.Data()
	def getIng(self):
		self.ing_list = self.data.inglist
	def getFood(self):
		self.food_list = self.data.foodlist
	def giveIng(self): #give the order of ingredients to model
		k = self.order_i.keys()
		for i in k:
			for j in self.ing_list:
				if k == j.name:
					j.amt = j.amt + self.order_i.get(k)
	def giveFood(self): #give the food cooked to model
		print "-"
	def getFood(self): #takes food from model. If not enough food, calls cook
		k = self.order_i.keys()
		temp = {}
		n = 0
		for i in k:
			for j in self.ing_list:
				if i == j.name:
					if self.order_i.get(k) > j.amt:
						n = self.order_i.get(k)/3
						if self.order_i.get(k)%3 > j.amt:
							n = n+1
					temp[i] = n
				n = 0
		self.cook(temp)
	def buyIng(self): #process stuff
		self.data.inglist = self.ing_list
		self.data.addIng(self.order_i.get("Ingredient"), self.order_i.get("Amount"))
		self.getIng()
		self.update_ing()
	def cook(self, food): #threading here. Cooks the food.
		n = 0
		print "Cooking your food. Please wait for" + str(n) + "seconds"
	def update_resto(self): #updates everything?
		self.getIng()
		self.getFood()
		self.update_ing()
	def update_ing(self): #updates the text file for ingredients
		self.getIng()
		f = open("ing.txt", "w")
		for i in self.ing_list:
			a = i + " = " + str(self.ing_list.amt) + "\n"
			f.write(a)
		f.close()
	def update_food(self): #updates the text file for cooked food
		self.getFood()
		f = open("fin.txt", "w")
		for i in self.food_list:
			a = i + ":" + str(self.food_list.amt) + "\n"
			f.write(a)
		f.close()

cc = CC()
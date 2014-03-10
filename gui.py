from Tkinter import*
import control
import model

class MainScreen:
	def __init__(self, root):
		self.cc = control.CC() 
	
		#self.menu = "YEY"
		self.ordered = {}
		
		root.geometry("640x480")
		root.title("Welcome to Pygkaithon!")
		
		resto = Frame(root, height=480, width=640)
		resto.place(x=0, y=0)
		
		kitchenMode = Button(resto, text="Go to the kitchen!", command=self.kitchen)
		kitchenMode.place(x=150, y=10)
		
		menuLabel = Label(resto, text="Menu:")
		menuLabel.place(x=10, y=15)
		
		menuScreen = Text(resto, width=50, height=20)
		menuScreen.insert(1.1, "Main Dishes:\n~Lasagna\n~Vegetarian Platter\n\nDesserts:\n~Banana Split\n~Sundae\n\nDrinks:\n~Bubble Tea\n~Chocolate Milkshake")
		menuScreen.config(state="disabled")
		menuScreen.place(x=10, y=50)
		
		label_1 = Label(resto, text="Choose your order: ")
		label_1.place(x=430, y=50)
		
		self.menulist = StringVar(resto)
		self.foodlist = ["order", "a", "b", "c"]
		self.menulist.set(self.foodlist[0])
		
		m = apply(OptionMenu, (resto, self.menulist)+tuple(self.foodlist))
		m.place(x=430, y=75)
		
		self.amt = StringVar(resto)
		self.amtnum = ["Amt"]
		for i in range(1, 4):
			self.amtnum.append(i)
		self.amt.set(self.amtnum[0])
		
		a = apply(OptionMenu, (resto, self.amt)+tuple(self.amtnum))
		a.place(x=530, y=75)
		
		order = Button(resto, text="Order", command=self.giveOrder)
		order.place(x=430, y=130)

	def giveOrder(self):
		foodOrder = self.menulist.get()
		amtOrder = self.amt.get()
		self.ordered["Food"] = foodOrder
		self.ordered["Amount"] = amtOrder
		self.cc.order_f = self.sendOrder()
	def sendOrder(self):
		return self.ordered
	def kitchen(self):
		self.ing_list = {}
		self.ing_list = self.get_ing()
		ingstr = str(self.ing_list)
		self.food_list = {}
		self.food_list = self.get_food()
		foodstr = str(self.food_list)
		
		kitchenScreen = Tk()
		
		kitchenScreen.geometry("460x320")
		kitchenScreen.title("Chef Mode")
		
		kc = Frame(kitchenScreen, height=320, width=460)
		kc.place(x=0, y=0)
		
		inglabel = Label(kc, text="Ingredients")
		inglabel.place(x=10, y=10)
		cookedlabel = Label(kc, text="Food")
		cookedlabel.place(x=230, y=10)
		
		ingtext = Text(kc, width=20, height=10)
		ingtext.place(x=10, y=50)
		ingtext.insert(1.1, ingstr)
		ingtext.config(state="disabled")
		foodtext = Text(kc, width=20, height=10)
		foodtext.place(x=230, y=50)
		foodtext.insert(1.1, foodstr)
		foodtext.config(state="disabled")
		
		buyinglabel = Label(kc, text="Buy:")
		buyinglabel.place(x=10, y=230)
		
		self.inglist = StringVar(kc)
		ingchoose = ["buy", "beef", "pasta", "cheese", "tomato", "cheese", "banana", "cream", "icecream", "chocolate"]
		self.inglist.set(ingchoose[0])
		
		m = apply(OptionMenu, (kc, self.inglist)+tuple(ingchoose))
		m.place(x=50, y=220)
		
		self.amt_i = StringVar(kc)
		amtnum = ["Amt"]
		for i in range(1, 11):
			amtnum.append(i)
		self.amt_i.set(amtnum[0])
		
		a = apply(OptionMenu, (kc, self.amt_i)+tuple(amtnum))
		a.place(x=50, y=250)
		
		ok_buy = Button(kc, text="Okay", command=self.buy_ing)
		ok_buy.place(x=50, y=285)
		
		cooklabel = Label(kc, text="Cook:")
		cooklabel.place(x=230, y=230)
		
		self.foodlist = StringVar(kc)
		foodchoose = ["buy", "lasagna", "vegplatter", "bananasplit", "sundae", "bbt", "chocomilkshake"]
		self.foodlist.set(foodchoose[0])
		
		o = apply(OptionMenu, (kc, self.foodlist)+tuple(foodchoose))
		o.place(x=270, y=220)
		
		ok_cook = Button(kc, text="Okay", command=self.cook)
		ok_cook.place(x=270, y=260)
		
		kitchenScreen.mainloop()
		
		self.data.update_resto()
	def get_ing(self):
		self.cc.getIng()
		return self.cc.ing_list
	def get_food(self):
		self.cc.getFood()
		return self.cc.food_list
	def buy_ing(self):
		self.ordered_i = {}
		ingorder = self.inglist.get()
		amtOrder = self.amt_i.get()
		self.ordered_i["Ingredient"] = ingorder
		self.ordered_i["Amount"] = amtOrder
		self.cc.order_i = self.sendOrder_i()
	def sendOrder_i(self):
		return self.ordered_i
	def cook(self):
		self.food2cook = {}
		foodcook = self.foodlist.get()
		self.food2cook["Food"] = foodcook
		self.cc.cookOrder = self.send2cook()
		print self.cc.cookOrder
	def send2cook(self):
		return self.food2cook
	

root = Tk()
mainScreen = MainScreen(root)
root.mainloop()
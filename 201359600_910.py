#Di po gumagana yung manual purchasing
from Tkinter import *
class Food():
    def __init__(self):
        self.name = ""
        self.kind = ""
        self.ing = {}
def open_ing(ing):
    file = open('ing.txt', 'r')
    #for x in file:
    #    print x
    for x in file:
        x = x.split("=")
        
        ing[x[0].strip()] = int(x[1].strip())
    file.close()
def open_fin(fin):
    file = open('fin.txt', 'r')
    for x in file:
        fin[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
    file.close()
#This is for Inventory.txt
def open_inven(ing, fin):
    curr = 1
    file = open("Inventory.txt","r")
    for x in file:
        if x == '\n':
            curr = 2
        elif curr == 1:
            ing[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
        elif curr == 2:
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
class Inventory():
    def __init__(self):
        self.ingredients = {}
        self.finished = {}
        open_ing(self.ingredients)
        open_fin(self.finished)
class Menu():
    def __init__(self):
        self.recipes = open_recipe()
class Window():
    def __init__(self):
        self.inven = Inventory()
        self.menu = Menu()

        self.order = {}
        for x in self.menu.recipes:
            self.order[x.name] = 0

        self.purch = {}
        for x in self.inven.ingredients:
            self.purch[x] = 0

        self.master = Tk()
        self.master.grid()
        self.master.geometry("300x600")
        
        self.Create_Widgets()
        self.See_Main()
        self.master.mainloop()
    def Create_Widgets(self):
        #main screen
        self.f_main = Frame(self.master)
        self.f_main.grid()
        Button(self.f_main, text = 'See Menu', command = self.See_Menu).grid(sticky = 'we')
        Button(self.f_main, text = 'See Inventory', command = self.See_Inven).grid(sticky = 'we')
        Button(self.f_main, text = 'Place Order', command = self.Goto_Order).grid(sticky = 'we')
        Button(self.f_main, text = 'Purchase Ingredients', command = self.Purch_Ing).grid(sticky = 'we')
        Button(self.f_main, text = 'Exit', command = self.Exit).grid(sticky = 'we')
        #menu screen
        self.f_menu = Frame(self.master)
        self.f_menu.grid()
        Label(self.f_menu, text = 'Main Course').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Main Course':
                Label(self.f_menu, text = x.name ).grid(sticky = 'w', column = 1)
                for y in x.ing:
                    Label(self.f_menu, text = str(x.ing[y]) + '   ' + y).grid(sticky = 'w', column = 2)
        Label(self.f_menu, text = 'Drinks').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Drinks':
                Label(self.f_menu, text = x.name ).grid(sticky = 'w', column = 1)
                for y in x.ing:
                    Label(self.f_menu, text = str(x.ing[y]) + '   ' + y).grid(sticky = 'w', column = 2)
        Label(self.f_menu, text = 'Dessert').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Dessert':
                Label(self.f_menu, text = x.name ).grid(sticky = 'w', column = 1)
                for y in x.ing:
                    Label(self.f_menu, text = str(x.ing[y]) + '   ' + y).grid(sticky = 'w', column = 2)
        self.b5 = Button(self.f_menu, text = 'Go Back', width = 40, command = self.See_Main)
        self.b5.grid(sticky = 'w', columnspan = 3)
        #inventory screen
        self.f_inven = Frame(self.master)
        self.f_inven.grid()
        Label(self.f_inven, text = 'Raw Ingredients').grid(sticky = 'w', column = 0)
        for x in self.inven.ingredients:
            Label(self.f_inven, text = str(self.inven.ingredients[x]) + '\t' + x).grid(sticky = 'w', column = 1)
        Label(self.f_inven, text = 'Finished Servings').grid(sticky = 'w', column = 0)
        for x in self.inven.finished:
            Label(self.f_inven, text = str(self.inven.finished[x]) + '\t' + x).grid(sticky = 'w', column = 1)
        self.b6 = Button(self.f_inven, text = 'Go Back', width = 40, command = self.See_Main).grid(sticky = 'w', columnspan = 2)
        #ordering screen
        self.f_order = Frame(self.master)
        self.f_order.grid()
        Label(self.f_order, text = 'Main Course').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Main Course':
                self.order[x.name] = IntVar()
                Checkbutton(self.f_order, text = x.name, variable = self.order[x.name]).grid(sticky = 'w', column = 1)
        Label(self.f_order, text = 'Drinks').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Drinks':
                self.order[x.name] = IntVar()
                Checkbutton(self.f_order, text = x.name, variable = self.order[x.name]).grid(sticky = 'w', column = 1)
        Label(self.f_order, text = 'Dessert').grid(sticky = 'w', column = 0)
        for x in self.menu.recipes:
            if x.kind == 'Dessert':
                self.order[x.name] = IntVar()
                Checkbutton(self.f_order, text = x.name, variable = self.order[x.name]).grid(sticky = 'w', column = 1)
        self.b7 = Button(self.f_order, text = 'Order', width = 40, command = self.Order_Up).grid(sticky = 'w', columnspan = 2)
        self.b8 = Button(self.f_order, text = 'Cancel', width = 40, command = self.Uncheck_Ord).grid(sticky = 'w', columnspan = 2)
        #purchasing ingredients screen
        self.f_purch = Frame(self.master)
        self.f_purch.grid()
        Label(self.f_purch, text = 'Ingredient').grid(row = 0, column = 0)
        Label(self.f_purch, text = 'Amount to buy').grid(row = 0, column = 1)
        curr_row = 1
        for x in self.purch:
            Label(self.f_purch, text = x).grid(row = curr_row, column = 0, sticky = 'w')
            self.purch[x] = StringVar()
            Entry(self.f_purch, textvariable = self.purch).grid(row = curr_row, column = 1)
            curr_row += 1
        Frame(self.f_purch, width = 40, bd = 1, relief = SUNKEN).grid(sticky = 'ws',pady = 5)
        Button(self.f_purch, text = 'Purchase', width = 40, command = self.Create_Purch).grid(sticky = 'w', columnspan = 2)
        Button(self.f_purch, text = 'Go Back', width = 40, command = self.See_Main).grid(sticky = 'w', columnspan = 2)
    def See_Main(self):
        self.f_main.grid()
        self.f_menu.grid_remove()
        self.f_inven.grid_remove()
        self.f_order.grid_remove()
        self.f_purch.grid_remove()
    def See_Menu(self):
        self.f_main.grid_remove()
        self.f_menu.grid()
        self.f_inven.grid_remove()
        self.f_order.grid_remove()
        self.f_purch.grid_remove()
    def See_Inven(self):
        self.f_main.grid_remove()
        self.f_menu.grid_remove()
        self.f_inven.grid()
        self.f_order.grid_remove()
        self.f_purch.grid_remove()
    def Goto_Order(self):
        self.f_main.grid_remove()
        self.f_menu.grid_remove()
        self.f_inven.grid_remove()
        self.f_order.grid()
        self.f_purch.grid_remove()
    def Purch_Ing(self):
        self.f_main.grid_remove()
        self.f_menu.grid_remove()
        self.f_inven.grid_remove()
        self.f_order.grid_remove()
        self.f_purch.grid()
    def Order_Up(self):
        for x in self.order:
            if self.order[x].get() == 1:
                if self.inven.finished[x] == 0:
                    self.Cook_Dish(x)
                else:
                    self.inven.finished[x] -= 1
                    notif = Notification(x, 'serve', 0)
        self.Uncheck_Ord()
        self.Update_Inven()
    def Cook_Dish(self, dish):
        curr_food = Food()
        for x in self.menu.recipes:
            if x.name == dish:
                curr_food = x
                break
        for x in curr_food.ing:
            if self.inven.ingredients[x] < curr_food.ing[x]:
                self.inven.ingredients[x] += 5
                notif = Notification(x, 'purch', 5)
                self.inven.ingredients[x] -= curr_food.ing[x]
            else:
                self.inven.ingredients[x] -= curr_food.ing[x]
        self.inven.finished[curr_food.name] += 2
        notif = Notification(curr_food.name, 'create', 0)
        notif = Notification(curr_food.name, 'serve', 0)
    def Update_Inven(self):
        self.f_inven.destroy
        self.f_inven = Frame(self.master)
        Label(self.f_inven, text = 'Raw Ingredients').grid(sticky = 'w', column = 0)
        for x in self.inven.ingredients:
            Label(self.f_inven, text = str(self.inven.ingredients[x]) + '\t' + x).grid(sticky = 'w', column = 1)
        Label(self.f_inven, text = 'Finished Servings').grid(sticky = 'w', column = 0)
        for x in self.inven.finished:
            Label(self.f_inven, text = str(self.inven.finished[x]) + '\t' + x).grid(sticky = 'w', column = 1)
        self.b6 = Button(self.f_inven, text = 'Go Back', width = 40, command = self.See_Main).grid(sticky = 'w', columnspan = 2)
    def Uncheck_Ord(self):
        for x in self.order:
            self.order[x].set(0)
        self.See_Main()
    def Create_Purch(self):
        for x in self.purch:
            print self.purch[x].get()
            if self.purch[x].get() != '':
                self.inven.ingredients[x] += int(self.purch[x].get())
                notif = Notification(x, 'purch', self.purch[x].get())
    def Exit(self):
        #self.Export_Inven()
        self.Export_Fin()
        self.master.destroy()
    def Export_Ing(self):
        file = open('ing.txt', 'w')
        for x in self.inven.ingredients:
            file.write(x + '=' + str(self.inven.ingredients[x]) + '\n')
        file.close()
    def Export_Fin(self):
        file = open('fin.txt', 'w')
        for x in self.inven.finished:
            file.write(x + ':' + str(self.inven.finished[x]) + '\n')
        file.close()
    def Export_Inven(self):
        file = open('Inventory.txt', 'w')
        for x in self.inven.ingredients:
            file.write(x + ':' + str(self.inven.ingredients[x]) + '\n')
        file.write('\n')
        for x in self.inven.finished:
            file.write(x + ':' + str(self.inven.finished[x]) + '\n')
        file.close()
class Notification():
    def __init__(self, obj, act, num):
        self.notif = Toplevel()
        self.notif.grab_set()
        if act == 'purch':
            Label(self.notif,  text = str(num) + obj + ' was just bought.').grid(sticky = 'news')
        elif act == 'serve':
            Label(self.notif, text = 'A/An ' + obj + ' was just served.').grid(sticky = 'news')
        elif act == 'create':
            Label(self.notif, text = '3 servings of ' + obj + ' was just made.').grid(sticky = 'news')
        elif act == 'no purch':
            Label(self.notif, text = 'No ' + obj + ' was bought.').grid(sticky = 'news')
        Button(self.notif, text = 'OK', command = self.press).grid(sticky = 'ws')
    def press(self):
        self.notif.grab_release()
        self.notif.destroy()
main = Window()

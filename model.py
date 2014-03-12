class Model():
    def __init__(self):
        self.inglist = Factory('ing').ret_comp()
        self.foodlist = Factory('food').ret_comp()
        
class Factory():
    def __init__(self, a):
        if a == 'ing':
            self.comp = self.open_Ing()
        else:
            self.comp = self.open_FoodRecipe()
    def ret_comp(self):
        return self.comp
    def open_Ing(self):
        list = []
        file = open('ing.txt', 'r')
        for x in file:
            x = x.split('=')
            list.append(Ingredient(x[0], x[1]))
        file.close()
        return list
    def open_FoodRecipe(self):
        list = []
        file = open('RecipeV2.txt', 'r')
        for x in file:
            try:
                if "\t" not in x:
                    list.append(temp)
                    temp = Food(x.split(':')[0].strip(), self.getAmt(x.split(':')[0].strip()))
                    temp.type = x.split(':')[1].strip()
                    temp.timeCooked = int(x.split(':')[2].strip())
                else:
                    temp.ings[x.split(":")[0].strip()]= int(x.split(":")[1].strip())
            except UnboundLocalError:
                temp = Food(x.split(':')[0].strip(), self.getAmt(x.split(':')[0].strip()))
                temp.type = x.split(':')[1].strip()
                temp.timeCooked = int(x.split(':')[2].strip())
        list.append(temp)
        file.close()
        return list
    def getAmt(self, name):
        file = open('fin.txt', 'r')
        for x in file:
            if x.split(':')[0].strip() == name:
                return int(x.split(':')[1].strip())
class Ingredient():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt
class Food(Ingredient):
    def __init__(self, name, amt):
        Ingredient.__init__(self, name, amt)
        self.type = ''
        self.timeCooked = 0
        self.ings = {}
'''
a = Model()
for x in a.foodlist:
    print x.name
    print 'amt: ' + str(x.amt)
    print 'type: ' + x.type
    print 'time: ' + str(x.timeCooked)
    print x.ings
'''
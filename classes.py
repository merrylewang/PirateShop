class Item:

    def __init__(self,name,price,type):
        self.name = name
        self.price = price
        self.number = 0
        self.type = type

class Shop:
    # creates a shop that has each movie as an Item object
    def __init__(self):
        fourD = Item("Star Wars Episode IV DVD ($20)", 20, "DVD")
        fiveD = Item("Star Wars Episode V DVD ($20)", 20, "DVD")
        sixD = Item("Star Wars Episode VI DVD ($20)", 20, "DVD")
        fourB = Item("Star Wars Episode IV Blu-Ray ($25)", 25, "Blu-Ray")
        fiveB = Item("Star Wars Episode IV Blu-Ray ($25)", 25, "Blu-Ray")
        sixB = Item("Star Wars Episode IV Blu-Ray ($25)", 25, "Blu-Ray")

        self.inventory = [fourD,fiveD,sixD,fourB,fiveB,sixB]

        self.numberInCart = 0
        self.cost = 0
        self.dvdset = set()
        self.dvdcount = 0
        self.blurayset = set()
        self.bluraycount = 0

    # adds one item into cart
    def add(self,product):
        self.cost += product.price
        self.numberInCart += 1
        if product.type == "DVD":
            self.dvdset.add(product)
            self.dvdcount += 1
        else:
            self.blurayset.add(product)
            self.bluraycount += 1

    # adds one item n times into cart
    def add_many(self,product,n):
        for _ in range(n):
            self.add(product)

    # completely empties cart
    def reset(self):
        self.numberInCart = 0
        self.cost = 0
        self.dvdset.clear()
        self.blurayset.clear()

    # applies discounts when cart includes all three DVDs or all three Blu-Rays
    def discounts(self):
        savings = 0
        if len(self.dvdset) == 3:
            dis = self.dvdcount * 0.1 * 20
            self.cost -= dis
            self.cost = round(self.cost,2)
            savings += dis

        if len(self.blurayset) == 3:
            dis = self.bluraycount * 0.15 * 25
            self.cost -= dis
            self.cost = round(self.cost, 2)
            savings += dis

        return savings


    # discount when you buy 100 or more items
    def bulkdiscount(self):
        savings = 0
        if self.numberInCart >= 100:
            dis = round(self.cost * 0.05,2)
            self.cost -= dis
            savings = dis
        return savings









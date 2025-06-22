#used in class methods where there can be multiple classes with same method name.
#class polymorphism
class Drsheths:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price 

    def rating(self):
        print("4.5")

class dot_and_key:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    def rating(self):
        print("3.5")

class Minimalist:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    def rating(self):
        print("4.6")

Drsheths1 = Drsheths(200, 150)
dot_and_key1 = dot_and_key(300, 150)
Minimalist1 = Minimalist(400, 100)

for brand in (Drsheths1, dot_and_key1, Minimalist1):
    brand.rating()

print(Drsheths1.quantity) #can be used to print attributes value

#example for polymorphism in inheritence
class skincare:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    def rating(self):
        print("4.5")

class cleanser(skincare):
    pass

class serum(skincare):
    def rating(self):
        print("4.8")

class facemask(skincare):
    def rating(self):
        print("4.7")

cleanser1 = cleanser(200, 100)
serum1 = serum(100, 200)
facemask1 = facemask(300, 400)
for items in (cleanser1, serum1, facemask1):
    items.rating()

print(cleanser1.quantity)
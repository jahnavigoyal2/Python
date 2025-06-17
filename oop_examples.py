#basic class and object 
class Skincare:
    company = "Dr.Sheths"
    def __init__(self, Type, price):# initialise attribute when new object created
        self.Type = Type
        self.price = price

product1 = Skincare("Cleanser", 200)
print(product1.company)
print(product1.Type)
print(product1.price)



class Skincare:
    company = "Dr.sheths"
    def __init__(self, Quantity, price):
        self.Quantity = Quantity
        self.price = price
    def details(self):
        print(f"the basic quantity of all products of {self.company} is {self.Quantity}ml and the price is {self.price}")
product1 = Skincare(75, 200)
product1.details()
product1.company = "dot and key"  #overridding class variable
print(product1.company)


class Skincare:
    company = "Dr.sheths"
    def __init__(self, Quantity, price):
        self.Quantity = Quantity
        self.price = price
    
product1 = Skincare(75, 200)
print(product1.company)
print(product1.Quantity,"ml")
print(product1.price)

product1.company = "dot and key"  #overridding class variable
print(product1.company)




class Skincare:
    company = "Dr.sheths"
    def __init__(self, Quantity, price):
        self.Quantity = Quantity
        self.price = price

class Cleanser(Skincare):   #single level inheritance
    def __init__(self, Quantity, price, skin_type):
        Skincare.__init__(self, Quantity, price)
        self.skin_type = skin_type

    def details(self):
        print(f"The cleanser of {self.company} is of {self.Quantity}ml and for {self.skin_type} type skin of price {self.price}.")

c1 = Cleanser(175, 250, "combination")
c1.details()

class foaming(Cleanser):
    def __init__(self, Quantity, price, skin_type, pH_level):
        super().__init__(Quantity, price, skin_type)
        self.pH_level = pH_level

    def info(self):
        print(f"The cleanser of {self.company} is of {self.Quantity}ml and for {self.skin_type} type skin of price {self.price} with the pH level of {self.pH_level}.")

foa = foaming(175, 250, "combination", 7.5)
foa.info()
    
class serum(Skincare):   #heirarchial inheritance
    def __init__(self, Quantity, price, shelf_life):
        Skincare.__init__(self, Quantity, price)
        self.shelf_life = shelf_life
    def information(self):
        print(f"The serum of {self.company} is of {self.Quantity}ml of price {self.price} and of {self.shelf_life} months.")
ser = serum(60, 300, 3)
ser.information()

class FaceMask(Cleanser, serum): #heirarchial inheritance
    def __init__(self, Quantity, price, skin_type, shelf_life, duration):
       
        Cleanser.__init__(self, Quantity, price, skin_type)
        serum.__init__(self, Quantity, price, shelf_life)
        self.duration = duration

    def insr(self):
        print(f"the face mask Quantity is {self.Quantity}ml for price of {self.price}  suitable for {self.skin_type} skin type having a shelf life {self.shelf_life}month and shoukd be used for {self.duration}min. ")

face = FaceMask(100, 100, "oily", 15, 15)
face.insr()


#encapsulation
class Sunscreen:
    def __init__(self, company, spf_level, price):
        self.company = company
        self.__spf_level = spf_level  #private
        self._price = price #protected

    def data(self):
        print(f"the sunscreen of {self.company} has the spf level of {self.__spf_level} and its cost is {self._price}")
sun = Sunscreen("Dr.sheths", "50 PA++", 150)
sun.data()


# to add attribute outside of class
class Skincare:
    company = "Dr.sheths"
    def __init__(self, Quantity, price):
        self.Quantity = Quantity
        self.price = price
    
product1 = Skincare(75, 200)
print(product1.company)
print(product1.Quantity,"ml")
print(product1.price)

product1.skin_type = "combination" 
print(product1.skin_type)
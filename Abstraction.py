from abc import ABC, abstractmethod
class Skincare(ABC):
    def __init__(self, company, price,):
        self.company = company
        self.price = price
    @abstractmethod
    def details(self):
       self

    def quality(self):
        print(f"the qualityy of {self.company} is good for average price {self.price}")

class Cleanser(Skincare):
    def details(self):
        print("company:",self.company)
        print("price:", self.price)
    
    def info(self):
        print("this much information in enough")
cl1 = Cleanser("Dr.sheths", 200)
cl1.details()
cl1.quality()
cl1.info()
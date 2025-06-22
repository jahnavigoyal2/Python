# define a method that bound to class not instance of class
# must have class as parameter

class skincare:
    total_brands = 0  # Class attribute

    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        skincare.total_brands += 1

    @classmethod
    def get_total_brands(cls):
        return cls.total_brands

    @classmethod
    def cleanser(cls, price):
        return cls(200, price)  # Assuming fixed quantity 200ml

# Object 
skincare1 = skincare(100, 150)
skincare2 = skincare(150, 100)
skincare3 = skincare.cleanser(300)  


print(f"Total brands: {skincare.get_total_brands()}")
print(f"Skincare 3 is a {skincare3.quantity}ml product priced at ₹{skincare3.price}")

class student:
    count = 0  

    def __init__(self, name):
        self.name = name
        student.increase_count()

    @classmethod
    def increase_count(cls):
        cls.count += 1
        
    @classmethod
    def display_count(cls):
        print(f"total students:{cls.count}")

s1 = student("jahnavi")
s2 = student("riddhi")

student.display_count()

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        return cls(day, month, year)
    
date1 = Date.from_string("19-06-2025")
print(date1.day, date1.month, date1.year)

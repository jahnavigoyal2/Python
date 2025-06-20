# define a method that bound to class not instance of class
# must have class as parameter

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

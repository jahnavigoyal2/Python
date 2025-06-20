# static method give information or does something without needing the  object
class toy:
    @staticmethod
    def wheels():
        print("most toys have 4 wheels")

toy.wheels()



class calculation():

    @staticmethod
    def addition (num1, num2):
        return num1 + num2 
    
result = calculation.add(10, 20)
print(result)
print(calculation.add(4, 6))


class skincare:
    brand = "Dr.sheths"
    
    @classmethod
    def class_method(cls):
        print("class method", cls.name)

    @staticmethod
    def static_method():
        print("static method: can not access anything",)

object = skincare()
object.static_method()
skincare.class_method()


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, student_str):
        name, age = student_str.split("-")
        return(name, age)
    def show(self):
        print(f"student name is {self.name} and age is {self.name}")

s1 = student.from_string("jahnaci", 20)

s1.show()

#from_string gets cls as first argument whoch is student_str
#then string is parsed inside that function
#and new object is returned using cls
# this is called factory method




# static method give information or does something without needing the  object

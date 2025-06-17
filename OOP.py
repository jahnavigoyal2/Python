class Student:   #class has the attributes and methods that object can have
    name = "jahnavi"
    
stu1 = Student()
print(stu1.name)

stu2 = Student()   
print(stu2.name)


class Car:
    color = "white"
    brand = "honda"
MyCar = Car()
print(MyCar.color)
print(MyCar.brand)


class Car:
    def __init__(self):
        self.name = "honda"
        self.color = "blue"
c1 = Car()
c2 = Car()
print(c1.__dict__)  #used to display in the form of key value pairs


class Car:
    def __init__(self, nam, col):
        self.name = nam
        self.color = col
c1 = Car("honda", "blue")
c2 = Car("toyota", "black")
print(c1.__dict__) 


class Person:
    name = "jahnavi"
    Occupation = "student"
    age = 20
    def info(self):
        print(f"{self.name} is a {self.Occupation} and of {self.age} years old.")
per1 = Person()
per2 = Person()
per1.name = "riddhi"
per1.age = 17

per2.name = "shyamani"
per2.age = 21
per1.info()
per2.info()


class Person:
    def __init__(self, n, o):
        self.name = n
        self.Occupation = o
    def info(self):
         print(f"{self.name} is a {self.Occupation}.")
        
per1 = Person("jahnavi", "student")
per2 = Person("riddhi", "student")
per1.info()
per2.info()


# dir method
class Person:
    def __init__(self, n, o):
        self.name = n
        self.Occupation = o
    def info(self):
         print(f"{self.name} is a {self.Occupation}.")
print(dir(Person)) #return list of all attributes and methods available for object
# print(Person.__setattr__)
per1 = Person("jahnavi", "student")
per2 = Person("riddhi", "student")
per1.info()
per2.info()

# __dict__ attribute
class person:
    def __init__(self, n, o):
        self.name = n
        self.Occupation = o
    def info(self):
        print(f"{self.name} is a {self.Occupation}.")

per1 = person("Jahnavi", "student")
per2 = person("riddhi", "student")
per1.info()
per2.info()
print(per1.__dict__)
print(per2.__dict__)

# Help() method
class person:
    def __init__(self, n, o):
        self.name = n
        self.Occupation = o
    def info(self):
        print(f"{self.name} is a {self.Occupation}.")

per1 = person("Jahnavi", "student")
per2 = person("riddhi", "student")
per1.info()
per2.info()
print(help(person))  #used to get help doc for object which has descri. of attribute and method

# without init 
class student:
    name = "jahnavi"
    age = 20
s1 = student()
print(s1.name)
print(s1.age)

# key diffrence is that without init the values for all objects will be fixed
#with init
class student:
    def __init__(self, name, age)
        self.name = name
        self.age = age
s1 = student("jahnavi", 20)
print(s1.name)
print(s1.age)


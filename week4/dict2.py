#dictionary
student = {"name":"jahnavi", "subject":"maths"}

#to access value from dictionary
student = {"name":"jahnavi", "subject":"maths"}
print(student["name"]) #if we try to access key that is not available then there will be keyerroe
print(student.get("age"))  #will not raise error will give none value

# to add or update key value pair
student = {"name":"jahnavi", "subject": "maths"}
student["age"] = 20  #to add new key value pair
student["age"] = 21  # to update value of existing key

# to remove
student = {"name":"jahnavi", "subject": "maths", "age": 20}
del student["age"]
print(student)

# to get all the key, value or pairs
student = {"name":"jahnavi", "subject": "maths"}
print(student.keys())
print(student.values())
print(student.items())

#to check if key exists
student = {"name":"jahnavi", "subject": "maths"}
if "subject" in student:
    print("yes its there")
else:
    print("does not exist")

#nested dictionaries
students = {"jahnavi":{"science": 80, "maths": 70},
            "riddhi":{"science": 80, "maths": 70},
            "shyamani":{"science": 80, "maths": 70}
            }

print(students["jahnavi"]["maths"])

#clearing all values of dict
student = {"name":"jahnavi", "subject": "maths"}
students2 = student.clear()
print(students2)

# copying a dictionary
student = {"name":"jahnavi", "subject": "maths"}
students = student.copy()
print(students)

# to iterate over a dictionary
student = {"name":"jahnavi", "subject": "maths"}
for key, value in student.items():
    print(f"{key}: {value}")

# to merge two dictionary
student = {"name":"jahnavi"}
student2 = {"subject": "maths"}
student.update(student2)
print(student)

# set default() method in dict
student = {"name":"jahnavi", "subject": "maths"}
default = student.setdefault("subject", "english")
print(student)

# default dictionary it is used to provide default value for a nonexistent key in the dictionary
from collections import defaultdict
student = defaultdict(int)
student["name"] = 1
print(student)

from collections import defaultdict

d = defaultdict(list)
d["fruits"].append("watermelon")
d["vegetables"].append("tomato")
print(d)

print(d["juice"])

#passing lambda
from collections import defaultdict
d = defaultdict(lambda: "value not present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

#dictionary with classes
class Skincare:
  def __init__(self, name, price):
        self.name = name
        self.price = price

items = {1:Skincare("cleanser", 1000),
         2:Skincare("serum", 1000),
         3:Skincare("facemask", 1000)
         }

print(items[2].price)

#dict from list

squares = {x: x**2 for x in range(1, 6)}
print(squares)

# to check how many methods
print(dir(int))  
print(dir(list))
#  dir list all attributes and methods available for an object 
# help provide detail in formation about an  object
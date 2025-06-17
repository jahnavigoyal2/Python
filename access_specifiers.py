#public access specifier
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student("jahnavi", 20)
print(s1.name)
print(s1.age)

#priate access specifier
class student:
    print(dir(student)) #for getting method of object
    def __init__(self, name, age):
        self.__name = name
        self.age = age
stu = student("jahnavi", 20)
# print(stu.__name) will not run as name is private
print(stu._student__name) # can be run due to name mangling in python
print(stu.age)
print(stu.__dir__())# to get methods of object 
 

#protected access specifer
class student:
    def __init__(self, name, age):
        self._name = name
        self.age = age
class subject(student):
    def __init__(self, name, age, faviorite_subject ):
        super().__init__(name, age)
        self.faviorite_subject = faviorite_subject
s1 = student("jahnavi", 20)
sub = subject("jahnavi", 20, "maths")
print(s1._name)
print(s1.age)
print(sub.faviorite_subject)
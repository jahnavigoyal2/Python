#method overloading using default argument
#python does not support method overloading by default
class student:
    def greet(self, name=None):
        if name:
            print("hello", name)
        else:
            print("hello")

s1 = student()
s1.greet()
s1.greet("jahnavi")

#method overloading using *arg
class calculation():
    def add(self, *args):
        return sum(args)
    
calc = calculation()
print(calc.add(5, 6))


#method overriding
class animal:
    def speak(self):
        print("animal makes sound")
class dog(animal):
    def speak(self):
        print("dog makes barking sound")
a1 = animal()
d1 = dog()
# a1.speak()
d1.speak()
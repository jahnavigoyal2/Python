students = ("jahnavi", "riddhi", "shyamani")
studentit = iter(students)  

print(next(studentit))   # next return the next item from the sequence
print(next(studentit))    # responsible for raiseing stop iteration exception
print(next(studentit))

students = "jahnavi"
studentsit = iter(students)

print(next(studentsit))
print(next(studentsit))
print(next(studentsit))
print(next(studentsit))
print(next(studentsit))
print(next(studentsit))
print(next(studentsit))
print(type(next(studentsit)))  


# to create object and class as iterator 
class numbers:
    def __iter__(self):  #returns the iterator object 
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a +=1
        return x
number1 = numbers()
iterate = iter(number1)

print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))


class numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
       if self.a <= 20:
        x = self.a
        self.a +=1
        return x
       else:
          raise StopIteration
       
number1 = numbers()
iterate = iter(number1)

for x in iterate:
   print(x)



students ["jahnavi", "riddhi"]
ite = iter(students)
 
while true:
   try:
      print(next(ite))
   except StopIteration: 
      print("stop")
      break
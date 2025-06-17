double = lambda x: x * 2
print(double(5))
cube = lambda y: y*y*y
print(cube(4))
sum = lambda x, y: x+y
print(sum(3, 5))


# map function using lamda
square = list(map(lambda x: x * x, [2, 4, 6, 8]))
print(square)

#filter using lambda
even = list(filter(lambda n: n%2==0, [1, 2, 3, 4, 5, 6, 7, 8] ))
print(even)

#reduce fubction using lambda
from functools import reduce
product = reduce(lambda x, y: x*y,[2, 4, 5, 6, 7, 8, 9, 10])
print(product)

# using lambda for condition cheacking
type = lambda x: "positive" if x > 0 else "negetive" if x < 0 else "zero"
print(8)

#using with list comprehension
product = [lamba arg = x:arg * 10 for x in range(1, 7)]
for i in list:
    print(i())


# with if else
check = lambda x: "even" if x%2==0 else "odd"
print(check(200))
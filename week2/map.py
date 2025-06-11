# map
def square(x):
    return x*x*x
l = [1, 2, 4, 6, 4, 3]
newl=list(map(square, l))
print(newl)


def even(n):
    return n%2==0
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
newlist = list(filter(even, list1))
print(newlist)

from functools import reduce
def product(x, y):
    return x*y
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(product, list2)
print(product)


marks = [1, 3, 5, 7]
marks2 = [2, 4, 6, 8]
marks3=marks.copy(marks2)
print(marks)
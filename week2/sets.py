s = {2, 4, 5, 5}
print(s)

harry = set()
print(type(harry))   # to create empty set 

details = {"jahnavi", 20, "female"}
for i in details:
    print(i)


numbers = {2, 4, 6, 8}
numbers2 = {1, 3, 5, 7}
print(numbers.union(numbers2))
print(numbers, numbers2)
numbers.update(numbers2)
print(numbers, numbers2)


states = {"gujrat", "maharashtra", "madhya pradesh"}
capital = {"gandhinagar", "mumbai", "bhopal"}
states2= states.union(capital)
print(states2)
states4=states.update(capital)
print(states4)
states3=states.intersection(capital)
print(states3)

states = {"gujrat", "maharashtra", "madhya pradesh"}
states2 = {"gujrat", "maharashtra", "madhya pradesh", "dehli", "andra pradesh"}
states3 = states.symmetric_difference(states2)
print(states3)
states5 = states.difference(states2)
print(states5)
print(states.isdisjoint(states2))
print(states.issuperset(states2))

states = {"gujrat", "maharashtra", "madhya pradesh"}
states2 = states.add("jammu")
print(states2)


states = {"gujrat", "maharashtra", "madhya pradesh"}
states3 = states.remove("gujrat")     # will raise erroe if item is not there in set 

states = {"gujrat", "maharashtra", "madhya pradesh"}
states3 = states.discard("maharshtra")  # will not raise error

states = {"gujrat", "maharashtra", "madhya pradesh"}
states2 = states.pop()
print(states2)  # we dont know which item will get poped as set is unordered


# states = {"gujrat", "maharashtra", "madhya pradesh"}
# del states
# print(states)  # get error as no set is defined


states = {"gujrat", "maharashtra", "madhya pradesh"}
if "gujrat" in states:
    print("gujrat is there in set")
else:
    print("gujrat is not there")
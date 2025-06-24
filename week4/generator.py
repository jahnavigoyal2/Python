#it is a special kind of functon that returns one value at a time using yeild keyword instaed of returning everything together using return.
#gives items one by one only when asked for them rathe than storing everything
#function that contains one or more yeild statements when run returns generator object which can be iterated over using next() or for

def generator():
    yield 1
    yield 2
    yield 3

new_gen = generator()
print(next(new_gen))
print(next(new_gen))
print(next(new_gen))


def generator():
    yield 1
    yield 2
    yield 3

for i in generator:
    print(i)

#example of genrator expression
square = (x*x for x in range(1,6))
for i in square:
    print(i)

def even_number_generator(limit):
    n=0
    while n<limit:
        yield n
        n +=2

for num in even_number_generator(20):
    print(num)


def generator(n):
    for i in range(n):
        yield i  #pause here and return value of i

for value in generator(20):
    print(num)


def infinite():
    num = 0
    while True:
        yield num
        num +=1 
def square(chain):
    for i in chain:
        yield num **2
def even(chain):
    for i in chain:
        if num % 2 ==0:
            yield i

numbers = infinite()
squared = square(numbers)
evens = even(squared)
        

for _ in range(20):  # _ is used because variable is not used in print statement
    print(next(evens))

# generator using break 
def generator():
    for i in generator(10):
        print(f"yeilding {i}")
        yield i

gen = generator()
for num in gen:
    if num ==5:
        print("Breaking here")
        break  #exits only the for loop not the generator
    print(num)
print("\n resuming from where it left\n")

for num in gen():
    print(num)

#to continue from where it left
# by default generator cant go backwards or rewind. once value is yielded it is gone from generator state

def generator():
    for i in generator(10):
        print(f"yeilding {i}")
        yield i

gen = generator()
for num in gen:
    if num ==5:
        print("Breaking here")
        break  #exits only the for loop not the generator
    print(num)
print("\n resuming from where it left\n")

gen = generator()  #recreate generator and go till 5 manually
for num in gen:
    if num<5:
        continue
    print(num)
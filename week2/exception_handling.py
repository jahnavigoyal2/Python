#zero division error
num1 = 10
num2 = 0
result = num1/num2
print(result)

#type error
num1 = 100
num2 = "jahnavi"
result = num1 + num2
print(result)


# try block 
# except Block
# else Block
# finally block


# Syntax
# try:
    #code 
# except[exception block]:
    #code to handle exeption
# else:
    #code to execute if no exception
# finally:
    # always executed



num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(result)
except [ZeroDivisionError]:
    print("divide by zero not possible")
print("always to be executed")


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(resul)
except [ZeroDivisionError]:
    print("divide by zero not possible")
except [NameError]:
    print("variable name wrong")
finally:
    print("always to be executed")

#here message of divide error will come even if name error
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(result)
except [ZeroDivisionError, NameError] :
    print("divide by zero not possible")
finally:
    print("always to be executed")


#message of the error that occured
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(result)
except [ZeroDivisionError, NameError] as obj:
    print(obj)
finally:
    print("always to be executed")


# this case if we dont know what error to define, can handle all error
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(result)
except:
    print("some error occured")
finally:
    print("always to be executed")


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1 / num2
    print(result)
except:
    print("some error occured")
else:
    print("no exeption occured")   # will execute only if no execute
finally:
    print("always to be executed")




num1 = int(input("enter first number "))
num2 = int(input("enter second number"))
try:
    result = num1/num2
    print("result")
except ZeroDivisionError as var:
    print(var.__class__)
print("remaining code")



num1 = int(input("enter first number "))
num2 = int(input("enter second number"))
try:
    result = num1/num2
    print("result")
except ZeroDivisionError as var:
    print(var)
    print(var.__class__)
print("remaining code")


import sys
num1 = int(input("enter first number "))
num2 = int(input("enter second number"))
try:
    result = num1/num2
    print("result")
except:
    print(sys.exc_info()[0])# class name error (will get exeption name)



import sys
num1 = int(input("enter first number "))
num2 = int(input("enter second number"))
try:
    result = num1/num2
    print("result")
except:
    print(sys.exc_info()[1])  #exeption information

try:
    l=[1, 3, 5, 7]
    j = int(input("enter the index:"))
    print(l[j])
except:
    print("some error occured")
finally:
    print("this will be executed")

# raising exception using raise keyword

try:
    age = int(input("enter your age:"))
    if age<0:
        raise ValueError
    print("your age is:", age)
except ValueError:
    print("enter valid age")

try:
    age = int(input("enter your age:"))
    if age<0:
        raise ValueError("invalid value entered")
    print("your age is:", age)
except ValueError as var:
    print(var)



#fiveDivisionError exeption
class fiveDivisionError(Exception):
    pass
try:
    num1 = int(input("enter first number "))
    num2 = int(input("enter second number"))
    if num2 == 5:
        raise fiveDivisionError("cannot divide with 5")
    result = num1/num2
    print(result)
except [ZeroDivisionError,fiveDivisionError] as var:
    print(var)





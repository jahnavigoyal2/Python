# print("hello world")
# print("jahnavi", 56, 56, sep="*")
# print("jahnavi", 67, end="9\n")
# print("jahnavi")

# x = 12345
# print(x)
# y = "jahnavi"
# print(type(y))

# b = True
# print(type(b))
# c = complex(8, 2)
# print(c)

# a = 10
# b = 20
# add = a+b
# print("the addition of two number is",add)
# sub = a-b
# print("the substraction of two number is", sub)
# mul = a*b
# print("the multiplication of two number is", mul)


# print(10, "+", 20, "=", 10 + 20)
# print(10, "-", 20, "=", 10 - 20)
# print(10, "/", 20, "=", 10 / 20)
# print(10, "*", 20, "=", 10 * 20)
# print(10, "%", 20, "=", 10 % 20)
# print(10, "**", 20, "=", 10 ** 20)


# a = "30"
# b = "40"
# print(int(a)+int(b))

# #inplicit type casting
# p = 3.5
# q = 4
# print(p+q)

# #input function i python
# # name = input("enter your name:")
# # print("my name is", name) 


# # number1 = int(input("enter the first number:"))
# # number2 = int(input("enter the second number:"))
# # print(number1 + number2)

# #strings in python
# name = "jahnavi"
# friend = 'riddhi' 
# text = 'he said "he wants to eat an apple".'
# multi_line = '''This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".
# This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".
# This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".
# '''
# print(name[3])     #indexing
# print (name[0])
# print(friend[5])
# # print(freind[10]) will give index error

# print("using for loop to index throug string")
# for characters in friend:
#     print(characters)

# # string methods
# names = "jahnavi, riddhi, shyamani"
# print(names[0:10])  #here 10 value will not show in output
# print(names[:8])
# print(names[0:])
# print(name[-4:-2])  #here -2 value wont show in output

# names = "jahnavi, riddhi"
# names1 = len(names)
# print("then length of the string is", names1)
# print(names.upper())
# print(names.lower())

# names = "**********jahnavi, riddhi**********"
# print(names.strip("*"))
# print(names.rstrip("*"))
# print(names.lstrip("*"))

# names = "jahnavi, riddhi"
# print(names.replace("riddhi", "shyamani"))
# print(names.split(","))    #split is used to make string into a list
# print(names.capitalize())  # capitalise first letter
# print(names.center(25))   # align the characters
# print(len(names.center(25)))
# print(names.count("a"))  # number of time something occured
# print(names.endswith("vi", 4, 7))

# # ways to concate string
# names="jahnavi, riddhi"
# friend = "shyamani"
# print(name + friend)   #+ operator
# together = f"{names},{friend}"  # f-string
# print (together)

# names="jahnavi, riddhi"
# names += "shyamani"   
# print(names)

# names=["jahnavi", "riddhi"]
# result = " ".join(names)
# print(names)

# names="jahnavi, riddhi"
# friend = "shyamani"
# result = "{} {}".format(names, friend)
# print (result)


# names="jahnavi, riddhi"
# friend = "shyamani"
# result = "%s %s" %(names, friend)
# print(result)

# names = "jahnavi and riddhi"
# print(names.find("vi"))
# print(names.find("issss"))
# print(names.index("vi"))
# print(names.isprintable())
# print(names.startswith("ja"))

# #conditional statememt
# # age = int(input("enter your age:"))    #imp to int define data type
# # print("your age is:", age)

# # if(age>18):
# #     print("you are eligible to vote")
# # else:
# #     print("you are not eligible to vote:")

# marks = 45
# if(marks >=90):
#     print("grade A")
# elif(marks >=80):
#     print("grabe B")
# else:
#     print("Grade c")

# marks = 56
# if (marks>=33):
#     print("congrats!!you passed")
#     if(marks>50):
#         print("excellent")
#     else:
#         print("average")
# else:
#     print("you have failed this time")

# # loop in python
# name = "jahnavi"
# for characters in name:
#     print(characters, end="-")

# name = "jahnavi"
# for characters in name:
#     print(characters)
#     if(characters=="n"):
#         print("this is in middle")
    
# for j in range(100):   
#    print(j)
#    print(j*2)

# for k in range(1, 12, 3):  #here 3 will define the gap between the two numbers that will come
#     print(k)


# i = 9
# while (i<15):
#     print(i)
#     i=i+1

# i = int(input("enter a anumber"))
# while(i<=10):
#     i = int(input("enter a number again"))
#     print(i)
# print("execution done")

# i = 5
# while(i>3):
#     print(i)
#     i = i-1
# else:
#     print("done")

# for i in range(12):
#     if (i==10):
#       break
#     print("5 x", i+1, "=", 5*(i+1)) 
# print("it left the remaining loop")


# for i in range(12):
#     if (i==10):
#       continue
#     print("5 x", i+1, "=", 5*(i+1)) 
# print("it left the iteration")

try:
    l=[1, 3, 5, 7]
    j = int(input("enter the index:"))
    print(l[j])
except:
    print("some error occured")
finally:
    print("this will be executed")

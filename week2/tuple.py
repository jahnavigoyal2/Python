# tup = (1, 3, 5, 7)
# print(tup)
# print(type(tup))


# tup = (1,)
# print(tup)  
# print(type(tup))  # coma after 1 is imp else vaue might be considered integer

# tup = (1, 3, 5, 7)
# print(tup)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])

# if 3 in tup:
#     print("it is there in this tuple")
# else:
#     print("no its not there")

# # methods of tuple
# tup = (1, 3, 5, 7)
# tem = list(tup)
# tem.append(9)
# tem.pop(1)
# tup = tuple(tem)
# print(tup )


# tup = (1, 3, 5, 7)
# res = tup.count(3)
# print(res)
# res2 = tup.index(3)
# print(res2)


# for i in range(10):
#     print(i)
#     if i==4:
#         break
# else:
#     print("sorry not in range")

# i = 0
# while i<7:
#     print(i)
#     i=i+1
# else:
#     print("loop fully executed")



# for x in range(10):
#     print("iteration no {} in for loop".format(x + 1))
# else:
#     print("out of loop")

# a = input("enter a number:")
# print(f"multiplication table for {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e:
#     print("Invalid input!")
# print("some imp lines of code")



# try:
#     num = int(input("enter an number:"))
#     a=[3, 4, 5, 6]
#     print(a[num])
# except ValueError:
#     print("entered number is not an integer")
# except IndexError:
#     print("there is an index error")


# try:
#     l=[1, 5, 6, 7]
#     i = int(input("enter the index:"))
#     print(l[i])
# except:
#     print("some error occurred")
# finally:
#     print("this part is always executed irrespective of the try and except")



# def func1():
#     try:
#         l=[1, 5, 6, 7]
#         i = int(input("enter the index:"))
#         print(l[i])
#         return 1
#     except:
#         print("some error occurred")
#         return 0
#     finally:
#         print("this part is always executed irrespective of the try and except")
# x = func1()
# print(x)



# marks = int(input("enter your marks:"))
# if marks(marks<33 or marks>50):
#     raise ValueError("please enter marks in between 33 to 50")


#short hand if else
marks = 3555
marks2 = 45
print("grade A") if marks>marks2 else print("=") if marks == marks2 else print("grade B")
marks3 = "average" if marks<marks2 else print("you need to work hard")
print(marks3)
print("good") if marks2>marks else " "
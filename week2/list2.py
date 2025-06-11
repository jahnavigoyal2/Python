marks = [34, 45, 56, 78]
print(marks)
print(type(marks))
print(marks[2])


student = ["jahnavi", "ahmedabad"] 
print(student)
student[1]="vadodra"
print(student)
print(student[1:2])
student.sort()
print(student)

marks = [34, 45, 56, 78]
marks.append(67)
print(marks)

marks = [33, 44, 55, 66]
print(marks.append(77))
print(marks.sort())
print(marks.sort(reverse=True))
print(marks)
marks.reverse()
print(marks)
marks.insert(2, 88)
print(marks)
marks.remove(44)
print(marks)
marks.pop(2)
print(marks)
marks2=marks.count(44)
print(marks2)


marks = [11, 22, 33, 44, 55, 66]
grades = marks.copy()
print(grades)



movies = []
mov1 = input("enter your first movie")
mov2 = input("enter your second movie")
mov3 = input("enter your third movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

movies = []
mov = input("enter your first movie:")
movies.append(mov)
mov = input("enter second movie")
movies.append(mov)
print(movies)


movies = []
movies.append(input("enter first movie:"))
movies.append(input("enter your second movie"))
movies.append(input("enter your third movie:"))

value = [1, 2, 3]
copyval = value.copy()
copyval.reverse()
if(copyval == value):
    print("its a palindrome")
else:
    print("not a palindrome")

# marks = [1, 3, 5]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# marks = [1, 3, 5]
# if 3 in marks:
#     print("yes it is there")
# else:
#     print("no it is not there")

# marks = [1, 3, 5]
# print(marks[:])
# # list comprehension
# num = [i+i for i in range(10)]
# print(num)
# num = [i+i for i in range(10) if i%2==0]
# print(num)

# marks = [1, 3, 5]
# marks.append(9)
# print(*marks)
# marks.sort()
# print(marks)
# print(marks.sort(reverse=True))
# print(marks.count(3))
# grade = marks.copy()
# print(grade)
# marks2 = marks.insert(2,7)

marks = [1, 3, 5, 7]
marks2 = [2, 4, 6, 8]
print(marks + marks2)
marks.extend(marks2)
print(marks)
for items in marks2:
    marks.append(items)
print(marks)


marks = [1, 3, 5, 7]
marks2 = [2, 4, 6, 8]
concatenated_list = [item for sublist in [marks, marks2]for item in sublist]
print(concatenated_list)

marks = [1, 3, 5, 7]
marks2 = [2, 4, 6, 8]
concatenated_list = [*marks, *marks2]
print(concatenated_list)
#static ways to convert list to string
students = ["ABC", "PQR", "XYZ"]
new_list = "ABC", "PQR", "XYZ"    #manual way
print(new_list)


students = ["ABC", "PQR", "XYZ"]
new_list = students[0]+','+students[1]+','students[2]
print(new_list)

# Dynamic way to covert list to string
students = ["ABC", "PQR", "XYZ"]
new_list = ",".join(students)    #using join() for string element
print(new_list)


marks = [70, 80, 90]
result = ",".join(str(elements)for elements in marks)
print(result)

marks = [70, 80, 90]
result = ",".join(map(str, marks))
print(result)
dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
print(dict)
print(dict["maharashtra"])
print(dict.get("gujrat"))
print(dict.get("dehli"))
print(dict.keys())
for key in dict:
    print(f"the value coresponding to {key} is {dict[key]}")

print(dict.values())
for value in dict:
    print(value)

print(dict.items())


dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
dict2 = {"madhya pradesh":"bhopal"}
dict.update(dict2)
print(dict)

dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
dict.clear()
print(dict)

dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
dict.pop("gujrat")
print(dict)

dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
dict.popitem()
print(dict)

dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
del dict["maharashtra"]
print(dict)

dict = {"gujrat":"gandhinagar", "maharashtra":"mumbai"}
del dict
print(dict)
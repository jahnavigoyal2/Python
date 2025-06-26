file = open("/Users/jahnavigoyal/Desktop/sample.txt", 'r')  # 'r' open for reading

data = file.read()
print(data)
print(type(data))
file.close()   # for closing the file

# 'w' open for writing truncating the file first
# to open binary file b needs to be written with other

file = open("/Users/jahnavigoyal/Desktop/sample.txt", 'r')  # 'r' open for reading
line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)
file.close()



file = open("/Users/jahnavigoyal/Desktop/sample.txt", 'r')  # 'r' open for reading

data = file.read(5)
print(data)
data = file.read(10)
position = file.seek(1)  # to go around agian

print(data)
data = file.read(1)
print(data)
print(position)
file.close()

with open("/Users/jahnavigoyal/Desktop/sample.txt", 'r') as file:
    for line in file:
        print(line)
        print(line.strip()) # to avoid whitspace
         
file = open("/Users/jahnavigoyal/Desktop/sample.txt", "w") # opening with w will overwrite the current contents
file.write("i am learning python")  
file.close()

file = open("/Users/jahnavigoyal/Desktop/sample.txt", "a") # this will add contents in the last
file.write("\nToday is my 4th week")
file.close()

# if there is no file of particular name but we use w or a command then it will create that particular file
# usinf r+ will open file for reading writing

file = open("/Users/jahnavigoyal/Desktop/sample.txt", "r+") # this will read and overwrite from start
file.write("today")
print(file.read())
file.close()

#if we open with w+ and then try to read then all data of file is deleted

file = open("/Users/jahnavigoyal/Desktop/sample.txt", "w+") # first will remove everything then agian add
print(file.read())
file.write("again i am learning python ")
file.close()

file = open("/Users/jahnavigoyal/Desktop/sample.txt", "a+") # first will not everything and then add at the end new text
print(file.read()) #here the pointer will be at last
file.write("again i am learning python ")
file.close()

with open("/Users/jahnavigoyal/Desktop/sample.txt", "r") as f:  # as means alias mean calling it something else same name other word
    data = f.read()
    print(data)

with open("/Users/jahnavigoyal/Desktop/sample.txt", "r") as f:
    f.write("today i will leran python")  
  

#to delete a file os module needs to be imported
# import tenserflow this cant be installed as its not pre installed

# import os
# os.remove("/Users/jahnavigoyal/Desktop/sample.txt")  this will remove or delete the file it cannot be deleted directly
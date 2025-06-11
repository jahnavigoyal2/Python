#walrus operatoe using loop
numbers=[1, 2, 3, 4, 5]
while (n := len(numbers))>0:
    print(numbers.pop())
#walrus operator usinng if statement
numbers=[1, 2, 3, 4, 5]
if (list_length := len(numbers))>4:
    print(f"the list has {list_length} elements, which is more than 4.")



#the key diffrence 
# with while it hwlps when we need to keep assigning and check in the loop and with if it assign value once and check once in desicion
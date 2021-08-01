#Enter your list of numbers
list_of_numbers = [1,2,2,3,2] 
list = []
for x in list_of_numbers:
    if x not in list:
        list.append(x)
print(list)
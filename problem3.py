str = input("please enter a string: ")
char = input("please enter a character: ")
n = -1
newlist = []
for x in str:
    n = n+1
    if x == char:
        newlist.append(int(n))
print(newlist)
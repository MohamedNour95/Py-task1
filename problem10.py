x=input("Please enter your name : ")
if x:
    print(x)
else:
    print('empty input')

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
y = input("Please enter your email: ")
if re.match(regex, y):
    flag = 1
else:
    print("invalid email please try again")
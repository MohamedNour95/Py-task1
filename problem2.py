s= input("please enter your string ")
v= ['a','e','i','o','u','y','A','E','I','O','U','Y']
x= ''
for i in s:
    if i not in v:
        x += i
print(x)
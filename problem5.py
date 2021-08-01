def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2
mystring = "anything" #put your string here
print('My string',mystring)
print('Split the string into two:',splitstring(mystring))
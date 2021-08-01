start = int (input("Please enter your start: "))
length = int (input("Please enter your length: "))
def output (start,length):
    arr = []
    for i in range(length):
        arr.append(start)
        start +=1
    return arr
print(output(start,length))
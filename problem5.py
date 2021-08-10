string = ("mohamed") #Please enter your string here

def split_str(string):
    str_len = len(string)
    
    if str_len % 2 == 0 :
        half = str_len / 2
        i = 0
        for c in range(len(string)):
            if i % half == 0:
              print('')
              print(string[c])
              i += 1
                
    else:
        half = str_len / 2
        first_half = round(half)
        i = 0
        for c in range(len(string)) :
            if i % first_half == 0 :
              print('')
            print(string[c])
            i += 1

split_str(string)

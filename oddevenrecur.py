# making function within the functTION

def ping(n):
    if (n%2 == 0):
       return True

    return False   


def printing(num):
    val = ping(num)
    if (val==True):
        print("no is even")
    else:
        print("no is odd") 

number = int(input())
printing(number)        

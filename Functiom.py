# method to count the elemts of array


ls = [2,4,56,42,4,5]
count = 0
for i in ls:
    count+=1
print (count)

# shortcut
print(len(ls))

# def nameoffun(parameter):
#return()

def length(ls):
    count = 0
    for i in ls:
       count+=1
    return count   

ls = [2,4,56,42,4,5,4,5]

for i in range(length(ls)):
    print(ls[i])


# print minimum
print("function for finding minimum")

def minimum(sush):
    mini=1000
    for i in sush:
        if i<mini:
          mini=i

    return mini

ls = [1,4,4,6,2,6,8,4]
print(minimum(ls))
print(min(ls))

print( "for sum of all element of sum")
sumof=0
for i in ls:
    sumof+=i

print(sumof)    

print(sum(ls))

#power functionj
print(2**10)
print(pow(2,10))

#function for power
print("function for power")
def power(value1,value2):
   return value1**value2

print(power(2,4))




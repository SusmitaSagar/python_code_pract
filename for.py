for x in "susmita":
    print(x)


fruit = """
s
u


a
"""
# no multiline comments, only unused string

print(fruit)
print(type(fruit))


for i in "susmita":
    print(i, end=" ")
# print("")


"range function"

for i in range(0, 9, 2):
    print(i)

for i in range (20):
 print(i)


#  sum of  i and j in loop  

for i in range(1, 5):
    for j in range(1, 5):
        print(i+j, end="")
    print("")


# average of number

n = int(input("enter any integer"))
sum=0
for i in range(0 , n+1):
    sum+=i

print(sum//n)


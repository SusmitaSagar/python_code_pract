# any type of value, dats can be stored
# ls = ["name", "tre", True, "90" , 0.33]
# print(ls)
# print(type(ls))
# ls = ["sagar","lily","sush","mani","hopw"]
# print(ls[2:4])
ls=[1,3,5,7,9,4]
# for i in range(len(ls)):
#     print(i)

maximum = -1
for i in ls:
    if maximum < i:
        maximum = i
print(maximum) 
print(max(ls))    
print (min(ls))

minimum = 100
for i in ls:
    if minimum >i:
        minimum=1
print (minimum)      

for i in ls:
    print(ls)

for i in ls:
    if i<ls:
        print(i)    

        



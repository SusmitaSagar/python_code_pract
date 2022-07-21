hi = "hello"
duniya = "Wordl"
#string are unmutable, means it cant be changed.
# 
"""
h    e     l        l      o
0    1     2        3       4
-5   -4    -3      -2      -1

"""
print(hi[1], hi[-2])

#we cant add or insert,chnage string by these methods below
# hi.append("e")
# print(hi)

# hi[3] = 'p'
# print(hi)

# name=input("enter your name:")
# print(hi + name)

# we append a value after the stirng
duniya += 'r'   #duniya=duniya+r
print(duniya)

duniya ="r"+duniya
# duniya = 99.93+duniya  # adding string and float, wrong
print(duniya)

# ls =[1,3,2,1,4,5]
# ls2=[7,4,5,4]
# print(ls+ls2)
# print(ls*3)
# print(ls*ls2) wrong statement

# slicing of string
# s= "my name is sushmia and i am an intelligent girl."
# print(s[:])
# print(s[1:])
# print(s[5:23])
# print(s[12:20])


# /////////////////////////////////////////////////////

string = "python lovers"
# print(string[2])

# s = "abc"
# print(s[3])  //this will throw eroor, out of range, \0 null chracter does not take any space

# for printing the index of given value of string
for i in range(len(string)):      # my mistakes  missed len,  and string keyword 
    if string[i] == 'l':
       print(i)

# short method //print index from starting
char = 'v'
print(string.find(char))

# for finding index of string from reverse
char = 'o'
print(string.rfind(char))  # reverse find
#if string not found, print -1

#////////////////////////////////////////////////////////////////

# chnage in uppercase
s="the Susmita sagar"
print(s.upper())
print(s.lower())

print(s.capitalize()) # print only first letter capital

print(s.split())  #make one elemnt of lidt if space in between
print(s.split('*'))  #make one 1st string as elemnt of list
print(s.count('a'))  #count the no of words came in  sntense

#///////////////////////
#zfill function will append 0 on actual value tilzfill parameter
stri2 ="er"
print(stri2.zfill(4))
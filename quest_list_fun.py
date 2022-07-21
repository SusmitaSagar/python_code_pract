# s=input()
# print(s)
# print(s.split())


# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    k=[]
    for i in range (N):
        p=input().split()
        if(p[0]== 'insert'):
            k.insert(int(p[1]),(int(p[2])))
        elif(p[0]=='print'):
            print(k)
        elif(p[0]=='remove'):
            k.remove(int(p[1]))
        elif(p[0]=='append'):
            k.append(int(p[1]))    
        elif(p[0]=='sort'):
            k.sort()
        elif(p[0]=='pop'):
            k.pop()
        elif(p[0]=='reverse'):
            k.reverse()
# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    miniSum=0
    maxSum=0
    for i in range(4):
        miniSum+=arr[i]
    print(miniSum,end=' ')    

    for i in range (4,0,-1):
        maxSum+=arr[i]
    print(maxSum)    
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
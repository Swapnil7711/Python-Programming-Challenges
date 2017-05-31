'''
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.


Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

length = len(arr)
count1 = 0
count2 = 0
count3 = 0
for i in range(length):
    
    if(arr[i] > 0):
        count1+=1
    if(arr[i]<0):
            count2+=1
    if(arr[i]==0):
            count3+=1

print(count1/n)
print(count2/n)
print(count3/n)
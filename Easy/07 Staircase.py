'''
Consider a staircase of size n:

   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
---------------------------------------------------

Input Format

A single integer, n, denoting the size of the staircase.

Output Format

Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######



'''

#!/bin/python3

import sys


n = int(input().strip())
p= n
for i in range(1,p):
    print(' '* (p-2),'#'*i)
    p-=1
print('#'*n)
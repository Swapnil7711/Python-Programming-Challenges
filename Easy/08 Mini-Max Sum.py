'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14


'''

#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

AllSum = sum(arr)    
print(AllSum - max(arr),AllSum - min(arr))
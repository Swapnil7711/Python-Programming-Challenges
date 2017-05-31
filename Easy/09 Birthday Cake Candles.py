'''
Colleen is turning n years old! She has n candles of various heights on her cake, and candle i has height H. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height H for each individual candle, find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer,n , denoting the number of candles on the cake. 
The second line contains n space-separated integers, where each integer i describes the height of candle i.
'''
#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
MaxHeight = max(height)
l = len(height)
count = 0
for i in range(l):
    if(height[i] == MaxHeight):
        count+=1
        
    
print(count)
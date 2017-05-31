'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
----------------------------------------------------------------------------
Sample Input

07:05:45PM
Sample Output

19:05:45

'''

#!/bin/python3

import sys
import datetime


time = input().strip()

arr = time.split(':')
if('PM' in time):
    if(arr[0]=='12'):
        arr[0] = arr[0]
        arr[2] = arr[2][0:2]
    else:
        arr[0] = int(arr[0])+12
        arr[2] = arr[2][0:2]
        
         

                        
if('AM' in time):
    arr[2]=arr[2][0:2]
    if('12' in time):
        arr[0] ='00'
        if(int(arr[0]) == 24):
            arr[0] ='00'
    
    
        
   
dt = datetime.time(int(arr[0]),int(arr[1]),int(arr[2])) 
print(dt)
#print(arr[0],':',arr[1],':',arr[2])
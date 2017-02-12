#!/bin/python3

import sys


time = input().strip()
if(time[-2::].upper() == 'PM' ):
    hours = int(time[:2])
    if(hours == 12):
        hours = "12"
        print(hours + time[2:-2])
    else:
        hours = 12 + hours
        hours = str(hours)
        hr_24time = hours+time[2:-2]
        print(hr_24time)
else:
    hours = int(time[:2])
    if(hours == 12):
        hours = "00"
        print(hours + time[2:-2])
    else:
        print(time[:-2])

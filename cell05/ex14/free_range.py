#!/usr/bin/env python3
import sys
x1=int(sys.argv[1])
x2=int(sys.argv[2])
list=[]
if len(sys.argv) == 3 :
    i = x1
    while i <= x2 :
        list.append(i)
        i+=1
    print(list)
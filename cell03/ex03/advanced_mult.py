#!/usr/bin/env python3
num = 0
while num < 11 :
    mult = 0
    print("Table de ", num , " : ",end =' ') 
    while mult < 11:
        total = num * mult
        print(total, end =' ')
        mult += 1
    num += 1
    print()

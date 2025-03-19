#!/usr/bin/env python3
import array as arr

new_array = arr.array('i',[])
first_array = arr.array('i',[2,8,10,9,7,6,5,3])
print("Original array : [2,8,10,9,7,6,5,3]")
print("New array : [",end='')
for i in first_array:
    new_array.append(i+2)
for i in new_array:
    print(f"{i},",end='')
print("]")



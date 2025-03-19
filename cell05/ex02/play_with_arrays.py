#!/usr/bin/env python3
import array as arr

i=0
new_array = arr.array('i',[])
first_array = arr.array('i',[2,8,10,9,7,6,5,3])
print("Original array : [2,8,10,9,7,6,5,3]")
print("New array : [",end='')

while i<len(first_array):

  if first_array[i] > 5:
    new_array.append(first_array[i]+2)
  i+=1
for num in new_array:
      print(f"{num},",end='')

#!/usr/bin/env python3
import array as arr

mylist = [2,8,9,48,8,22,-12,2]
mylist1 = set(mylist)
i=0
new_array = arr.array('i',[])
first_array = arr.array('i',mylist1)
print(f"Original array : {mylist}")
print("New array : [",end='')

while i<len(first_array):

  if first_array[i] > 5:
    new_array.append(first_array[i]+2)
  i+=1
for num in new_array:
      print(f"{num},",end='')
print("]")


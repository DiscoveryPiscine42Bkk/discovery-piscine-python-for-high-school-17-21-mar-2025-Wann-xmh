#!/usr/bin/env python3
import sys
x = len(sys.argv)
# print(len(sys.argv))
print(f"parameters : {x-1}")

for i in range(1,x):
    print(f"{sys.argv[i]} : {len(sys.argv[i])}")

    #   print(sys.argv[i],end=' ')
    print(len(sys.argv[i]))

#!/usr/bin/env python3
import sys
if len(sys.argv) > 2:
    for i in range(2,len(sys.argv)) :
       print(sys.argv[i])
else :
    print("none")
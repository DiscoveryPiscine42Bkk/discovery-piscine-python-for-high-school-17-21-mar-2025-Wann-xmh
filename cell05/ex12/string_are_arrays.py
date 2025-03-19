#!/usr/bin/env python3
import sys
import re

x=0
i = len(re.findall('z',sys.argv[1]))
if i > 0 :
    while x < i:
        print("z",end='')
        x+=1



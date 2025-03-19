#!/usr/bin/env python3
import sys
import re

# i=1
if len(sys.argv) > 1 :
  for i in range(1, len(sys.argv)):
    parameter = sys.argv[i]
    if len(re.findall('ism',parameter)) > 0:
        True
    else:
        print(f"{parameter}ism")
else:
   print("none")

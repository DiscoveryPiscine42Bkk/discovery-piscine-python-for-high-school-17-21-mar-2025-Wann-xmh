#!/usr/bin/env python3
import re
import sys

s = sys.argv[1]
sentence = sys.argv[2]
r1 = re.findall(s,sentence)
print(len(r1))
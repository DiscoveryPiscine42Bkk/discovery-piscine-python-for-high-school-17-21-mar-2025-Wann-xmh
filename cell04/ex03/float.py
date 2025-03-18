#!/usr/bin/env python3
number = input("Give me a number : ")
number = float(number)
num = int(number)
str_number = str(number)
str_num = str(num)

if str_number == str_num:
    print("This number is an integer.")
else:
    print("This number is a decimal.")



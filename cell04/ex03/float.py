#!/usr/bin/env python3
number = input("Give me a number : ")
number = float(number)
num = int(number)

if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")



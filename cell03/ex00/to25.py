#!/usr/bin/env python3
number = int(input("Enter number less than 25 : "))

if number < 25 :
    while number <= 25 :
        print("Inside the loop , my variable is ", end = ' ')
        print(number)
        number += 1
else :
    print("Error")

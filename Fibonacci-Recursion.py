# -*- coding: utf-8 -*-
"""
In mathematics, the Fibonacci Sequence is a sequence in which each number is the
sum of the two preceding ones

Created on Tuesday April 23 18:43:27 2024
@author: Shon Harsh

Example Sequences:
F0 = 0
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
F13 = 233
F14 = 377
F15 = 610
F16 = 987
F17 = 1597
F18 = 2584
F19 = 4181
"""
def calculateFibonacciNumber(number):
    # validate input; negative
    if number < 0:
        print("Incorrect input")
 
    # validate input; 0
    elif number == 0:
        return 0
 
    # validate input; 1 or 2
    elif number == 1 or number == 2:
        return 1
 
    #recurse
    else:
        return calculateFibonacciNumber(number-1) + calculateFibonacciNumber(number-2)
  
# invoke fibbonacci
inputNumber = 20
print("Fibonacci", str(inputNumber), "=", calculateFibonacciNumber(inputNumber))
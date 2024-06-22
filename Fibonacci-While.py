# -*- coding: utf-8 -*-
"""
In mathematics, the Fibonacci Sequence is a sequence in which each number is the
sum of the two preceding ones

Created on Tuesday April 23 18:34:35 2024
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

def calculateFibonacci(number):

    count = 1
    number1 = 0
    number2 = 1
    number_next = number2

    #loop
    while count < number:
        print(number_next, end=" ")
        count = count + 1
        number1 = number2
        number2 = number_next
        number_next = number1 + number2

    return number

# invoke fibbonacci
inputNumber = 20
print("Fibbinacci", inputNumber)
calculateFibonacci(inputNumber)

"""
1. Return the first, last, smallest, largest, and average of five user given integers.
2. Ask users for a username and determine if it is included in a given list of usernames, if so, print 'Access is
granted', if not, print 'Access is denied'.

Total Income. Created by Malia, March 2021.
"""

# 1. Basic list operations
numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter your username: ")

if username in usernames:
    print("Access granted")

else:
    print("Access denied")

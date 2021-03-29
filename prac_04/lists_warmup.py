numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0]) # Prints the 1st element in the list = 3
print(numbers[-1]) # Prints the last element in the list = 2
print(numbers[3]) # Prints the 4th element in the list = 1
print(numbers[:-1]) # Prints the list in order, exluding the last element = [3, 1, 4, 1, 5, 9]
print(numbers[3:4]) # Slices the list before the 3rd element and after the 4th element = [1]
print(5 in numbers) # Checks if the integer 5 is present in the list = True
print(7 in numbers) # Checks if the integer 7 is present in the list = False
print("3" in numbers) # Checks if the string "3" is present in the list = False
print (numbers + [6, 5, 3]) # Prints the list with 6, 5, and 3 added to the end = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
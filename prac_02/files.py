#1
name = input("Please enter your name: ")
name_file = open("name.txt", 'w')
print(name, file=name_file)
name_file.close()

#1
name_file = open("name.txt", "r")
first_line = name_file.read().strip()
print("Your name is {}".format(first_line))
name_file.close()

#3
number_file = open("numbers.txt", "w")
print("17\n42\n400", file=number_file)
number_file.close()

number_file = open("numbers.txt", "r")
first_line = int(number_file.readline())
second_line = int(number_file.readline())
number_file.close()
print(first_line + second_line)

number_file = open("numbers.txt", "r")
total_number = 0
for line in number_file:
    number = int(line)
    total_number += number
print(total_number)

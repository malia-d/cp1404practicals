"""
Print the same number of asterisks as there are characters in a user inputted password, with error checking for
the minimum length.

Password Check. Created by Malia, March 2021.
"""

MINIMUM_LENGTH = 6


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Please enter your password, containing at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        password = input("Your password doesn't contain enough characters.\nPlease enter your password, containing at "
                         "least {} characters: ".format(minimum_length))
    return password


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end='')


main()

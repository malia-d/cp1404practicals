import random

NUMBERS_PER_LINE = 6
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1


def main():
    """Display a user given number of lines, with six digits each that range from 1 to 45."""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_picks = []
        # generate a random number between the minimum and maximum values
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            # replaces any numbers that have already appeared in the list
            while number in quick_picks:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()  # sorts the numbers in ascending order
        # print the list with a space separating each number, six numbers per line, and the user given number of lines
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()

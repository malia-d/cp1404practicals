"""


Guitars. Created by Malia, April 2021.
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print("{} ({}) : ${:.2f} added.".format(name, year, cost))
        name = input("Name: ")


main()

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

    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
            print("Guitar {}: {} ({}), worth ${:.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
        else:
            print("Guitar {}: {} ({}), worth ${:.2f}".format(i + 1, guitar.name, guitar.year, guitar.cost))


main()

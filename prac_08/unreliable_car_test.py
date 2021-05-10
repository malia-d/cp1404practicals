"""
Test the Unreliable Car class by creating two cars, one with high reliability and one with low reliability. Test both
cars multiple times and print the distance each car has driven.

Unreliable Car Test. Created by Malia D'Mello, May 2021.
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test Unreliable Car class."""
    first_car = UnreliableCar("Prius 1", 100, 95)
    second_car = UnreliableCar("Kia Rio", 100, 5)

    for i in range(1, 11):
        print("Attempting to drive {}km:".format(i))
        print("{:2} drove {:2}km".format(first_car.name, first_car.drive(i)))
        print("{:2} drove {:2}km".format(second_car.name, second_car.drive(i)))

    print(first_car)
    print(second_car)


main()

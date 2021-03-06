"""
Print the car details, using the Car class to change the fuel and odometer values, and use string formatting.

Used Cars. Created by Malia, April 2021.
"""

from prac_06.car import Car


def main():
    """Use the Car class to print car details."""
    my_car = Car("Sedan", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)


main()

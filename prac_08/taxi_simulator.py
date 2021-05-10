"""
Ask the user to select from a menu, inputting the number of the taxi chosen and the distance the taxi is being driven.
After each trip, the user will be given the trip fare, as well the total bill to date. When the user decides to quit,
the program will end by displaying the total trip cost and listing the taxis now available.

Taxi Simulator. Created by Malia D'Mello, May 2021.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Execute a taxi trip."""
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_selection = input(">>> ").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            print("Taxis available:")
            display_taxi_list(taxis)
            taxi_selection = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_selection]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_selection == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_driven = float(input("Drive how far? "))
                current_taxi.drive(distance_driven)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        menu_selection = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxi_list(taxis)


def display_taxi_list(taxis):
    """Display the formatted list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()

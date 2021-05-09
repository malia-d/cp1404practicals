"""
Test the Taxi class by creating a taxi and modifying the distance driven.

Taxi Test. Created by Malia D'Mello, May 2021.
"""

from prac_08.taxi import Taxi


def main():
    """Test Taxi class"""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)


main()

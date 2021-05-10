"""
Test the Silver Service Taxi class by creating a silver service taxi with a fanciness of 2. Print the silver service
taxi fare.

Silver Service Taxi Test. Created by Malia D'Mello, May 2021.
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxi class"""
    fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print("${:.2f}".format(fancy_taxi.get_fare()))


main()

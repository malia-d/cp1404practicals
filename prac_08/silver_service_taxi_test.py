from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print("${:.2f}".format(fancy_taxi.get_fare()))


main()

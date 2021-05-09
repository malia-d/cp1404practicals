"""
Create a Silver Service Taxi class, derived from parent class Taxi. Return the total silver service taxi fare, taking
into account the fanciness of 2 and the flagfall class variable.

Silver Service Taxi. Created by Malia D'Mello, May 2021.
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    """Represent a Silver Service Taxi object."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return the Silver Service Taxi with the flagfall class variable."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the total Silver Service Taxi fare."""
        return self.flagfall + super().get_fare()

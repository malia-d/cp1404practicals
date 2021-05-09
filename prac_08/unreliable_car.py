"""
Create an Unreliable Car class, derived from parent class Car. Generate a random float number between 0 and 100 and only
drive the car a given distance if it's reliability is greater than the random number. Otherwise, return 0km driven.

Unreliable Car. Created by Malia D'Mello, May 2021.
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Represent an Unreliable Car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the Unreliable Car a given distance if it's reliability is greater than the random float number
        generated."""
        random_number = random.uniform(1, 100)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

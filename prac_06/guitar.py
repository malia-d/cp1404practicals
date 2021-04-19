"""
Determine how old a Guitar is, and if it is vintage (older than 50 years), and return the Guitar details using string
formatting.

Guitar. Created by Malia, April 2021.
"""

CURRENT_YEAR = 2021


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar details using string formatting."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Determine Guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage."""
        return self.get_age() >= 50

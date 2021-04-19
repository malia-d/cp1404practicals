"""
Determine if a Programming Language's 'typing' is dynamic and return the Programming Language details using string
formatting.

Programming Language. Created by Malia, April 2021.
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""
    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the Programming Language's 'typing' is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return Programming Language details using string formatting."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

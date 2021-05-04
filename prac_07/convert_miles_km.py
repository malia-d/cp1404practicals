"""
Display a program converting a user-inputted distance in miles to kilometers. Increase and decrease miles value by 1
when buttons pressed. When an invalid value is inputted, display 0 km.

Convert Miles to Km. Created by Malia D'Mello, May 2021.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = "Malia D'Mello"

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """MilesToKmApp is a Kivy App for converting miles to km."""
    output_km = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation, output km value."""
        miles = self.handle_invalid()
        self.root.ids.output_km.text = str(miles * MILES_TO_KM)

    def handle_modify(self, miles_change):
        """Handle modification by 1, increase or decreased value by 1."""
        miles = self.handle_invalid() + miles_change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def handle_invalid(self):
        """Handle invalid miles input, return miles as a float value, or as 0.0."""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


MilesToKmApp().run()

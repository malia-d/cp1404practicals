"""
Display a program squaring a user-inputted integer value. Display "Invalid Input" when a non-integer value is entered.

Squaring. Created by Lindsay Ward, October 2015. Modified by Malia D'Mello, May 2021.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number."""
    def build(self):
        """ Build the Kivy app from the kv file. """
        Window.size = (400, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Input"


SquareNumberApp().run()

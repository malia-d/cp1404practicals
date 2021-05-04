"""
Display a program asking a user to enter their name. Upon pressing 'greet', Greet the user by name. Allow the user
to clear all fields.

Box Layout Demo. Created by Lindsay Ward. Modified by Malia D'Mello, May 2021.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App for greeting a user by name."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting user, output greeting with user name."""
        print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle clearing fields, output blank input and output fields."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()

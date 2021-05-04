"""
Display a program displaying a list of names as labels.

Dynamic Labels. Created by Malia D'Mello, May 2021.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

___author__ = "Malia D'Mello"


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App for displaying a list of names as labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Anna Adams', 'Bob Brown', 'Claire Campbell', 'Daniel Davies', 'ELizabeth Elliot']

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name in a list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.names.add_widget(temp_label)


DynamicLabelsApp().run()

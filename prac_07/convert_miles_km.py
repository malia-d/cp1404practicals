from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = "Malia D'Mello"

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.handle_invalid()
        self.root.ids.output_km.text = str(miles * MILES_TO_KM)

    def handle_modify(self, miles_change):
        miles = self.handle_invalid() + miles_change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def handle_invalid(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


MilesToKmApp().run()

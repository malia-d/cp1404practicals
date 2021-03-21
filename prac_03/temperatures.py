"""
Convert between Celsius and Fahrenheit based on user inputs, with error checking for invalid inputs,
and the option to quit the program.

Temperatures. Created by Malia, March 2021.
"""

MENU = """C - Convert Celsius to Fahrenheit 
F - Convert Fahrenheit to Celsius 
Q - Quit"""


def main():
    """Print menu, ask user to make a selection and to input starting temperature, and print conversion result."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit_conversion(celsius)
            print("Result: {:.2f} F".format(fahrenheit))  # String formatting to display result to 2 decimal places
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius_conversion(fahrenheit)
            print("Result: {:.2f} C".format(celsius))  # String formatting to display result to 2 decimal places
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit_conversion(celsius):
    """Calculate and return Celsius to Fahrenheit conversion."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius_conversion(fahrenheit):
    """Calculate and return Fahrenheit to Celsius conversion."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

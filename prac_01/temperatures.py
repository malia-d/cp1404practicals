"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32  # Calculate celsius to fahrenheit conversion
        print("Result: {:.2f} F".format(fahrenheit))  # String formatting to display result to 2 decimal places
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)  # Calculate fahrenheit to celsius conversion
        print("Result: {:.2f} C".format(celsius))  # String formatting to display result to 2 decimal places
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

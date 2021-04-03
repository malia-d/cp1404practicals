"""
This program receives a user input, colour_name, and if it is contained within the dictionary, NAME_TO_CODE, it prints
the colour name and code, and continues to prompt the user for a new input. If it is not contained in the dictionary, it
prints an invalid input message and prompts the user for a new input.

Hex Colours. Created by Malia, April 2021.
"""

NAME_TO_CODE = {"AliceBlue": "f0f8ff", "pink": "ffc0cb", "LightSlateBlue": "8470ff", "gold1": "ffd700",
                "firebrick2": "ee2c2c", "MediumPurple1": "ab82ff", "PaleGreen2": "90ee90", "tan1": "ffa54f",
                "gray1": "030303", "white": "ffffff"}

colour_name = input("Enter colour name: ")
# While the user input is not blank the loop proceeds, but if the user input is blank the loop stops.
while colour_name != "":
    # If the colour_name is in NAME_TO_CODE the loop prints the colour name and its code, then asks for another input.
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    # If colour_name is not in NAME_TO_CODE the loop prints an invalid message and asks for another input.
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")

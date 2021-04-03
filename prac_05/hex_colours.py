"""
Receive a user input, colour_name, and if it is contained within the dictionary, NAME_TO_CODE, print the colour name and
code, and prompt the user for a another input. If the dictionary does not contain the colour code, print an invalid
input message and prompt the user for a another input.

Hex Colours. Created by Malia, April 2021.
"""

NAME_TO_CODE = {"AliceBlue": "f0f8ff", "pink": "ffc0cb", "LightSlateBlue": "8470ff", "gold1": "ffd700",
                "firebrick2": "ee2c2c", "MediumPurple1": "ab82ff", "PaleGreen2": "90ee90", "tan1": "ffa54f",
                "gray1": "030303", "white": "ffffff"}

colour_name = input("Enter colour name: ")
# While user input is not blank the loop will proceed, but if user input is blank the loop will stop.
while colour_name != "":
    # Print the colour name and its code.
    if colour_name in NAME_TO_CODE:
        print("{} is {}".format(colour_name, NAME_TO_CODE[colour_name]))
    # Print an invalid message.
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")

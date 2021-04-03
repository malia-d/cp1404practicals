NAME_TO_CODE = {"AliceBlue": "f0f8ff", "pink": "ffc0cb", "LightSlateBlue": "8470ff", "gold1": "ffd700", "firebrick2":
    "ee2c2c", "MediumPurple1": "ab82ff", "PaleGreen2": "90ee90", "tan1": "ffa54f", "gray1": "030303", "white": "ffffff"}
print(NAME_TO_CODE)

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")

"""
Receive a user input, state_code, and if it is contained within the dictionary, CODE_TO_NAME, it prints the full state
name, and continues to prompt the user for a new input. If it is not contained in the dictionary, it prints an invalid
input message and prompts the user for a new input. It also contains a 'for' loop that prints all of the state
abbreviations and their full names, lined up using string formatting.

State Names. Created by Malia, April 2021.
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    # If state_code is in CODE_TO_NAME the loop prints the state code and its full name, then asks for another input.
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    # If state_code is not in CODE_TO_NAME the loop prints an invalid message and asks for another input.
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# A loop that prints all of the state abbreviations and their full names neatly lined up with string formatting.
for state_code in CODE_TO_NAME:
    print("{0:3} is {1:1}".format(state_code, CODE_TO_NAME[state_code]))

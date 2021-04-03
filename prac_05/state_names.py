"""
Receive a user input, state_code, and if it is contained within the dictionary, CODE_TO_NAME, print the state name
abbreviation and the full state name, and continue to prompt the user for a new input. If the dictionary does not
contain the state name, print an invalid input message and prompt the user for a new input. The 'for' loop will print
all of the state name abbreviations and their full names, lined up using string formatting.

State Names. Created by Malia, April 2021.
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
# While user input is not blank the loop will proceed, but if user input is blank the loop will stop.
while state_code != "":
    # Print the state code and its full name, and ask for another input.
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    # Print an invalid message and ask for another input.
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all state abbreviations and their full names, lined up with string formatting.
for state_code in CODE_TO_NAME:
    print("{:3} is {:1}".format(state_code, CODE_TO_NAME[state_code]))

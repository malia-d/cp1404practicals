"""
Ask the user to input an email address and extract a name from it. Then ask the user if the extracted name is correct.
If the user input is 'Y', 'y' or blank ask for another email. If the input is anything else, ask the user to input the
name and ask for another email. Store the name and email as as key/value pairs in the dictionary. Once the user email
input is blank print each name with it's corresponding email.

Emails. Created by Malia, April 2021.
"""


def main():
    """Create a dictionary of emails, as keys, and names, as values, and print them using string formatting."""
    email_to_name = {}
    email = input("Email: ")
    # While user input is not blank the loop will proceed, but if user input is blank the loop will stop.
    while email != "":
        name = get_name_from_email(email)
        name_check = input("Is your name {}? (Y/n) ".format(name))
        if name_check.upper() != "Y" and name_check != "":  # check if the user input is not "Y" or blank
            name = input("Name: ")
        email_to_name[email] = name  # add the name and email to the dictionary
        email = input("Email: ")
    # Iterate through the dictionary and print each key/value pair.
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Get the name from the email address."""
    parts = email.split("@")[0]
    parts = parts.split(".")
    name = " ".join(parts)
    name = name.title()  # capitalize the first letter of the first and last name
    return name


main()

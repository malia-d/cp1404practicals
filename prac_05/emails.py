def main():
    """Create a dictionary of emails as keys and names as values, and print them using string formatting. """
    email_to_name = {}
    email = input("Email: ")
    # While the user input is not blank the loop proceeds, but if the user input is blank the loop stops.
    while email != "":
        name = get_name_from_email(email)
        name_check = input("Is your name {}? (Y/n) ".format(name))
        if name_check.upper() != "Y" and name_check != "":  # checking if the user input is not "Y" or blank
            name = input("Name: ")
        email_to_name[email] = name  # adding the name and email to the dictionary
        email = input("Email: ")
    # Iterates through the dictionary printing each key/value pair.
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Get the name from a user inputted email address."""
    parts = email.split("@")[0]
    parts = parts.split(".")
    name = " ".join(parts)
    name = name.title()  # capitalizes the first letter of the first and last name
    return name


main()

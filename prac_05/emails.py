def main():
    """Create a dictionary of emails as keys and names as values, and print them using string formatting. """
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_check = input("Is your name {}? (Y/n) ".format(name))
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Get the name from a user inputted email address."""
    parts = email.split("@")[0]
    parts = parts.split(".")
    name = " ".join(parts)
    name = name.title()
    return name


main()

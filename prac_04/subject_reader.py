"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Obtain the subject data as a list and display it one list per line."""
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        print("----------")
    input_file.close()
    return data


def display_subject_details(data):
    """Print the subject, lecturer and number of students enrolled in the subject."""
    for subject_details in data:
        print("{} is taught by {:1} and has {:2} students".format(*subject_details))


main()

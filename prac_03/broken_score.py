"""
Receive a user inputted score, and a randomly generated score, and print the corresponding results.

Broken Score. Created by Malia, March 2021.
"""


def main():
    """Receive scores and print their corresponding results."""
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    score = random.randint(0, 100)  # Generate a random score
    print(determine_score_status(score))


def determine_score_status(score):
    """Return the result that corresponds with the score."""
    # If the score is greater than or equal to 90, or less than or equal to 100, print "Excellent"
    if 90 <= score <= 100:
        return "Excellent"
    # If the score is greater than or equal to 50, or less than or equal to 89, print "Passable"
    elif 50 <= score <= 89:
        return "Passable"
    # If the score is greater than or equal to 0, or less than or equal to 59, print "Bad"
    elif 0 <= score <= 49:
        return "Bad"
    else:
        return "Invalid score"


main()

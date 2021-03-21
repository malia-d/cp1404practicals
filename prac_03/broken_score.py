"""
Receive a user inputted score, and a randomly generated score, and print the corresponding results.

Broken Score. Created by Malia, March 2021.
"""

score = float(input("Enter score: "))
# If the score is greater than or equal to 90, or less than or equal to 100, print "Excellent"
if 90 <= score <= 100:
    print("Excellent")
elif score >= 50:
    print("Passable")
elif score >= 0:
    print("Bad")
else:
    print("Invalid score")

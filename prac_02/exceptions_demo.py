"""CP1404/CP5632 - Practical Answer the following questions:
1. When will a ValueError occur?
It will occur if you try to enter a character that it not an integer, such as a floating-point number or a letter.

2. When will a ZeroDivisionError occur?
It will occur if you enter zero as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, this can be done by, in the event of zero being entered as the denominator, asking the user to re-enter a
denominator value other than zero.
 """

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please enter a denominator other than zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

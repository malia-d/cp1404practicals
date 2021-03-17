MIN_LENGTH = 6

user_password = input("Please enter your password: ")

password_length = len(user_password)

while password_length < MIN_LENGTH:
    print("Your password must contain a minimum of 6 characters")
    user_password = input("Please enter your password: ")
    password_length = len(user_password)

else:
    for i in range(password_length):
        print("*", end='')

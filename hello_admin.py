#RyanWaltersDev May 12 2021 -- TIY 5-8 5-9

#Check for empty list, print admin message, print general
usernames = ['admin', 'bababooey', 'siiiickboi', 'bigdoinks', '420blazemaster']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome back Admin. Would you like to see the status report?")
        else:
            print(f"Hello {username}! Welcome back. Thanks for choosing our "
            "website")
else:
    print("We really need some users!")

#END OF PROGRAM

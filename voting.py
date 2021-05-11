#RyanWaltersDev May11 2021 -- Simple conditional voting age test

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register as soon as you turn 18!")

registration = 'yes'
if registration.lower() == 'yes':
    print("Great! You can vote at this booth.")
else:
    print("Ok, let's get you registered.")

#END OF PROGRAM

#RyanWaltersDev May 11 2021 -- if-elif-else

age = 32

if age < 4:
    print("Your cost of admission is free!")
elif age < 18 or age >= 65:
    print("Your cost of admission is $25.")
else:
    print("Your cost of admission is $40.")

#Rewriting code block to be more concise
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40

print(f"Your cost of admission is ${price}.")

#Revising code block to omit the else statement
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your cost of admission is ${price}.")

#END OF PROGRAM

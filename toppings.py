#RyanWaltersDev -- Apr8 2021 -- Checking for Inequality Ch5

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Using the 'in' keyword to check for an item in a list
requested_toppings = ['sausage', 'extra cheese', 'spinach']
if 'mushrooms' in requested_toppings:
    print("Add mushrooms to that pie baby!")
else:
    print("Hold the mushrooms!")

#Testing multiple conditions with if statements
if 'sausage' in requested_toppings:
    print("Let's get some sausage on this za!")
if 'extra cheese' in requested_toppings:
    print("Say cheese! Let me see some extra!")
if 'spinach' in requested_toppings:
    print("Throw in some spin baby! Yeah! Spinach!")
if 'pepperonni' in requested_toppings:
    print("Pepper up these ronis!")

#Running out of an item
requested_toppings = ['pepperonni', 'extra cheese', 'green peppers', 'sausage']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry bozo! Out of peppers!")
    else:
        print(f"Adding {requested_topping}!")

print("Pizza's done!")

#Making sure the list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}!")
    print("\nPizza's done!")
else:
    print("Are you sure you want a plain pizza bro?")

#Establishing available toppings to check for unavailable toppings
avilable_toppings = ['extra cheese', 'pepperonni', 'sausage', 'green peppers',
'onions', 'olives', 'pineapple']
requested_toppings = ['extra cheese', 'green peppers', 'tictacs']
for requested_topping in requested_toppings:
    if requested_topping in avilable_toppings:
        print(f"Adding {requested_topping}!")
    else:
        print(f"I'm sorry, we can't add {requested_topping} to your pizza.")
print("Pizza's done!")

#END OF PROGRAM
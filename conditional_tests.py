#RyanWaltersDev May10 2021 Try it yourself 5-1 and 5-2

#Initial True and False for beer
beer = 'bud light'
print("Is beer == 'bud light'? I predict True.")
print(beer == 'bud light')

print("\nIs beer == 'michelob'? I predict False.")
print(beer == 'michelob')

print("\nIs beer == 'pabst'? I predict False.")
print(beer == 'pabst')

#Not equal tests
print("\nIs beer != 'bud light'? I predict False.")
print(beer != 'bud light')

print("\nIs beer != 'michelob'? I predict True.")
print(beer != "michelob")

print("\nIs beer != 'pabst'? I predict True.")
print(beer != 'pabst')

#True and False with a list?
beer = ['miller lite', 'michelob', 'sweetwater']
print("\nIs beer == 'michelob'? I predict True")
print(beer == 'michelob')
print("\nI was wrong. Maybe the entire list is necessary.")
print(beer == ['miller lite', 'michelob', 'sweetwater'])

#True and False with strings
string = 'Hello world.'
print("\nIs the string == 'Hello world.'? I predict True")
print(string == 'Hello world.')
print("\nIs the string == 'Goodbye world.'? I predict False.")
print(string == 'Goodbye world.')
print("\nTesting if the string is case sensitive. If yes, the interpreter "
    "will return False.")
print(string == 'hello World.')

#Using the .lower() method to do a test
beers = ['miller lite', 'michelob', 'sweetwater', 'bud light', 'dos equis']
beer = 'DOs EquIs'
if beer.lower() in beers:
    print(f"\nYes! We currently have {beer.title()} in stock.")

#And or tests with the beer list
beer1 = 'MILLER LITE'
beer2 = 'bud light'
beer3 = 'Terrapin Hopsecutioner Double IPA'

if beer1.lower() and beer2.lower() in beers:
    print(f"\nYes! We have both of those beers in stock.")

if beer1.lower() or beer3.lower() in beers:
    print(f"\nWe have one of those beers in stock.")

#Testing whether a beer is or is not in a list
print(f"\nDo you have {beer1} in stock?")
if beer1.lower() in beers:
    print(f"\nYes. We have {beer1.title()} in stock.")

print(f"\nDo you have {beer3} in stock?")
if beer3.lower() not in beers:
    print(f"\nNo. We would never carry {beer3.title()}. It is a horrible trash "
        "beer.")

#Conditional tests using numerical values
user_answer = 75

if user_answer != 42:
    print(f"\nYour answer is {user_answer}. This is incorrect! Lets compare.")

if user_answer > 42:
    print(f"\nYour answer is {user_answer}, which is greater than the correct "
        "response.")
else:
    print(f"\nYour answer is {user_answer}, which is not greater than the "
        "correct response.")

if user_answer < 42:
    print(f"\nYour answer is {user_answer}, which is less than the correct "
        "response.")
else:
    print(f"\nYour answer is {user_answer}, which is not less than the correct "
        "response.")

if user_answer == 42:
    print(f"\nCongratulations! You have answered 42, which is correct!")
else:
    print(f"\nSorry. The answer we were looking for is 42. You must now go on "
        "with the rest of your life in shame, living in the shadow of this "
        "moment in which you ultimately, deicdedly, failed.")


#END OF PROGRAM

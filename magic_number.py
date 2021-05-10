#RyanWaltersDev -- Apr8 2021 -- Conditional Number Test Ch5

#Inequality operator
answer = 22

if answer != 42:
    print("You have answered incorrectly. Please, try again!")

#Trying different mathematical comparisons. Messing around with else.
answer = 19
print(f"Your answer is {answer}. Let's compare it to the number 21.")

if answer < 21:
    print("Your answer is less than 21.")
else:
    print("Your answer is not less than 21.")

if answer <= 21:
    print("Your answer is less than or equal to 21.")
else:
   print("Your answer is not less than or equal to 21.") 

if answer > 21:
    print("Your answer is greater than 21.")
else:
    print("Your answer is not greater than 21.")

if answer >= 21:
    print("Your answer is greater than or equal to 21.")
else:
    print("Your answer is not greater than or equal to 21.")

#Trying with the and keyword
answer_1 = 22
answer_2 = 19

if (answer_1 >= 21) and (answer_2 >= 21):
    print("Your answers are both greater than 21.")
else:
    print("At least one of your answers is not greater than 21.")

answer_2 = 25

if (answer_1 >= 21) and (answer_2 >= 21):
    print("Your answers are both greater than 21.")
else:
    print("At least one of your answers is not greater than 21.")

#Trying with the or keyword
answer_1 = 23
answer_2 = 18

if (answer_1 >= 21) or (answer_2 >= 21):
    print("At least one of your answers is greater than 21.")
else:
    print("Neither of your answers are greater than 21.")

answer_1 = 19

if (answer_1 >= 21) or (answer_2 >= 21):
    print("At least one of your answers is greater than 21.")
else:
    print("Neither of your answers are greater than 21.")

#END OF PROGRAM

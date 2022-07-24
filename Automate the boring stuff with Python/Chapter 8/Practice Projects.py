"""
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip

menu = {"wheat": 2, "white": 3, "sourdough": 2, "chicken": 2, "ham": 3, "tofu": 4, "turkey": 1,
        "cheddar": 1, "swiss": 1, "mozarella": 1, "mayo": 1, "mustard": 1, "lettuce": 1, "tomato": 1, }

order = []

order.append(pyip.inputMenu(["wheat", "white", "sourdough"]))

order.append(pyip.inputMenu(["chicken", "turkey", "ham", "tofu"]))

if pyip.inputYesNo("Do you want cheese with your order? ") == "yes":

    order.append(pyip.inputMenu(["cheddar", "swiss", "mozarella"]))

if pyip.inputYesNo("Do you want mustard with your order? ") == "yes":
    order.append("mustard")

if pyip.inputYesNo("Do you want mayo with your order? ") == "yes":
    order.append("mayo")

if pyip.inputYesNo("Do you want lettuce with your order? ") == "yes":
    order.append("lettuce")

if pyip.inputYesNo("Do you want tomato with your order? ") == "yes":
    order.append("tomato")

numSandwiches = pyip.inputInt("How many sandwiches do you want?", min=1)

total = 0
for menuItem in order:
    total += menu[menuItem]

print(f'Total price: ${total * numSandwiches}')


"""
Write Your Own Multiplication Quiz
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project 
on your own without importing it. This program will prompt the user with 10 multiplication questions, 
ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
"""


import time
import random
import sys
import time
print("Welcome to the Multiplication Game!")
numberOfQuestions = 0
correctAnswers = 0

if input("If you want to start a new round press 'y' \n") == "y":
    while True:
        if numberOfQuestions > 9:
            print(f"number of correct anwsers is {correctAnswers}/10")
            if input("Do you want to play another round? (y/n)") == "y":
                numberOfQuestions = 0
                correctAnswers = 0
                continue
            else:
                break
        randomNum1 = random.randint(0, 9)
        randomNum2 = random.randint(0, 9)
        print(f"What's the result of {randomNum1} and {randomNum2}?")
        wrongTries = 0
        startTimer = time.time()
        while True:
            try:
                if wrongTries > 2:
                    print("too many wrong tries; on to the next question")
                    numberOfQuestions += 1
                    time.sleep(1)
                    break
                res = int(input())
                endTimer = time.time()
                if endTimer - startTimer > 8:
                    print("Out of time! \n next question!")
                    numberOfQuestions += 1
                    time.sleep(1)
                    break
                if res == randomNum1 * randomNum2:
                    print("Correct!")
                    numberOfQuestions += 1
                    time.sleep(1)
                    correctAnswers += 1
                    wrongTries = 0
                    break
                else:
                    print("Wrong answer! \n Try Again!")
                    wrongTries += 1
            except:
                print("please enter an integer")

    correctAnswers = 0
    numberOfQuestions = 0
else:
    sys.exit()

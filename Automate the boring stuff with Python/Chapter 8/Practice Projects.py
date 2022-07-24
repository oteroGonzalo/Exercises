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

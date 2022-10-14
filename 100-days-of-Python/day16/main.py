from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import pyinputplus as pypi

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menuItems = (menu.get_items() + "off" + "/report").split("/")
print(menuItems)
while True:
    userChoice = pypi.inputChoice(menuItems)
    if userChoice == 'off':
        break
    elif userChoice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else: 
        if coffeeMaker.is_resource_sufficient(menu.find_drink(userChoice)) and moneyMachine.make_payment(menu.find_drink(userChoice).cost):
                coffeeMaker.make_coffee(menu.find_drink(userChoice))








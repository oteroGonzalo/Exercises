import pyinputplus as pyip

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000, 
    "milk": 1000,
    "coffee": 1000,
    "money": 0
    }
    
unit = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    }
coinsValue = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01
    }
    
missingIngredients = []
    
    
def isMissingResources(userChoice):
    for item in MENU[userChoice]['ingredients']:
        if resources[item] < MENU[userChoice]['ingredients'][item]:
            missingIngredients.append(item)
    return bool(len(missingIngredients))
    
def payment(userChoice):

    quarters = pyip.inputNum('How many quarters are you going to insert?: ')
    dimes = pyip.inputNum('How many dimes are you going to insert? ')
    nickles = pyip.inputNum('How many nickels are you going to insert ')
    pennies = pyip.inputNum('How many pennies are you going to insert ')
    
    totalAmount = quarters*coinsValue["quarter"] + dimes*coinsValue["dime"] + nickles*coinsValue["nickle"] + pennies*coinsValue["penny"] 
    
    if totalAmount < MENU[userChoice]['cost']:
        return f'${totalAmount} is not enough money'
    else:
        for ingredient in MENU[userChoice]['ingredients']:
            resources[ingredient] -=  MENU[userChoice]['ingredients'][ingredient]
            
        resources['money'] += MENU[userChoice]['cost']
        change = round(totalAmount - MENU[userChoice]['cost'], 2)
        
        return(f'Here is your {userChoice} and your change is ${change}. Enjoy!')
        

while (True):
    
    userChoice = pyip.inputChoice(['espresso', 'latte', 'cappuccino', 'report', 'off'], 
    prompt="What would you like? (espresso/latte/cappuccino):\n")
    
    if userChoice == 'off':
        print('Coffee machine has been turned off')
        break
    elif userChoice == 'report':
        
        report = ""
        
        for resource in resources:
            if resource == "money":
                report += f'Money: ${resources["money"]}'
            else:
                unitOfResource = unit[resource]
                report += f'{resource.capitalize()}: {resources[resource]}{unitOfResource}\n'
            
        print(report)
        
    else:
        
        if isMissingResources(userChoice):
            print(f'not enough {missingIngredients}')
        else:
            print(payment(userChoice))
            
    




        

    
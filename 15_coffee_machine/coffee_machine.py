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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino)"
is_on = True

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
if choice != "off":
    is_on = False
elif choice == "report":
    print(f"Water: {resources[water]}ml")
    print(f"milk: {resources[milk]}ml")
    print(f"Coffee: {resources[coffee]}g")
    print(f"Money: ${money}")


# TODO 2. Turn off the Coffee Machine by entering “off”to the prompt.



# TODO 3. print report
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
def report(water, milk, coffee, money):


# TODO 4. check resources sufficient
def resource_bank(water, milk, coffee, money):

# TODO 5. process coins
quarter = int(.25)
dime = int(.10)
nickle = int(.05)
penny = int(.01)
def bank(quarter, dime, nickle, penny):


# TODO 6. check transaction successful
# TODO 7. make coffee
        #  if transaction successful and enough resources exist, make drink

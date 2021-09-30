from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#starting of the code 

# example of menu item class
# one_item = MenuItem('latte', 100, 0, 16, 1.5)
# # one_item.name = 'Your mom'
# # one_item.cost = 1.5
# # one_item.ingredients = {'water': 100, "coffee": 16}
# print(one_item)

# print(one_item.name)
# print(one_item.cost)
# print(one_item.ingredients)


# example of menu class
# list_class = Menu()
# print(list_class)

# print(list_class.get_items())
# print(list_class.find_drink('cappuccino'))


# tinkering with the moneymachine class
# print()
# print('---------------')
# print('money machine class')
# money_record = MoneyMachine()
# print('record of object being created')
# print(money_record)
# money_record.report()
# money_record.make_payment(1.5)
# money_record.report()

#----------------------
# messing with CoffeMaker class
# print()
# print('--------------')
# print('CoffeeMaker Class')
# coffee_actions = CoffeeMaker()
# coffee_actions.report()
# print(coffee_actions.is_resource_sufficient(one_item))
# coffee_actions.make_coffee(one_item)
# coffee_actions.report()


# officially starting the project

# Making the 3 objects - name, water, milk, coffee, cost
latte_item = MenuItem('latte', 200, 150, 24, 2.5)
espresso_item = MenuItem('espresso', 50, 0, 18, 1.5)
cappuccino_item = MenuItem('cappuccino', 250, 100, 24, 3.0)

print(f"These are the 3 items we have:\n{latte_item}\n{espresso_item}\n{cappuccino_item}")
print(f"Name: {latte_item.name}\nCost: {latte_item.cost}\nIngredients: {latte_item.ingredients}")
print(f"Name: {espresso_item.name}\nCost: {espresso_item.cost}\nIngredients: {espresso_item.ingredients}")
print(f"Name: {cappuccino_item.name}\nCost: {cappuccino_item.cost}\nIngredients: {cappuccino_item.ingredients}")

# asking user and recieving response also using the menu class to determine whether they did or didn't type it right
menu_checking = Menu()
user_input = input(f'What would you like? ({menu_checking.get_items()}): ').lower()
user_response_error = False
# print(menu_checking.find_drink(user_input))
# loop starts for checking correct wording
while not user_response_error:
    if menu_checking.find_drink(user_input):
        print("This is true: meaning that it has created or found an object")
        user_response_error = True
    else:
        user_input = input("Please select another item on the menu: ")
    
print('You have successfully escaped the loop')

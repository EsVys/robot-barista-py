
items_without_milk = {
    'espresso': 2.00,
    'lungo': 2.50,
    'doppio': 3.00
}

items_without_milk_cold = {
    'cold brew': 2.50
}

items_with_milk = {
    'latte': 4.00,
    'cappuccino': 3.50
}

babyccino_price = 1.50

def format_menu(items: dict):
    return ', '.join(f'{name.capitalize()} {price} €' for name, price in items.items())

items_without_milk_str = format_menu(items_without_milk)
items_without_milk_cold_str = format_menu(items_without_milk_cold)
items_with_milk_str = format_menu(items_with_milk)

def ask_yes_no(prompt: str):
    answer = input(prompt).lower()
    if answer == 'yes':
        return True
    if answer == 'no':
        return False
    print('The value is not correct, please choose yes or no.')
    return ask_yes_no(prompt)

def add_milk(price_without_milk: float):
    if ask_yes_no('Do you wish to add oat milk?\n'):
        return price_without_milk + 0.25
    return price_without_milk

def easter_egg_david():
    if ask_yes_no(f'David? You started drinking coffee?\n'):
        print('Wait, really? Someone alert the press.')
        get_order('David')
    else:
        print('Oh, it is for Ester! Thank you!')
        get_order('Ester')

def offer_babyccino(name: str):
    prompt = f'We are sorry, {name}, we cannot offer you caffeinated drinks. Would you like to have a babyccino?\n'
    if ask_yes_no(prompt):
        print(f'The price is {babyccino_price} €.')
        final_print('babyccino', 1)
    else:
        print('Okay then. Come back when you are older!')
        print('\n\nNext please!')

def get_order(name: str):
    print(f'Here is our menu. \n{items_without_milk_str}, {items_without_milk_cold_str}, {items_with_milk_str}.')
    order = input('What would you like?\n').lower()

    #price calculation
    if order in items_without_milk:
        price = add_milk(items_without_milk[order])
    elif order in items_without_milk_cold:
        price = add_milk(items_without_milk_cold[order])
    elif order in items_with_milk:
        price = items_with_milk[order]
    else:
        print('Sorry, we do not have that here.\n\nNext please!')
        return
    quantity = validate_input_quantity()
    total = float(price) * float(quantity)
    print(f'The price is {total} €.')
    final_print(order, quantity)
    return order, quantity

def validate_input_quantity():
    quantity = input('How many coffees would you like?\n')
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print('The value is not correct, only positive numbers are allowed.')
            return validate_input_quantity()
        return quantity
    except ValueError:
        print('The value is not correct, only numbers are allowed.')
        return validate_input_quantity()

def final_print(order, quantity):
    if quantity == 1:
        print(f'We will have your {order} ready in a minute.')
    else:
        print(f'We will have your {quantity} {order}s ready in a minute.')
    hot_warning(order)
    print('\n\nNext please!')

def hot_warning(order):
    if not order in items_without_milk_cold:
        print('Be careful, the drink is hot.')

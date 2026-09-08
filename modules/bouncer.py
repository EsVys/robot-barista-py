import modules.barista as barista


def age_validation(age: int, name: str):
    if age < 16:
        barista.offer_babyccino(name)
        return False
    return True

def validate_input_age(name):
    age = input(f'What is your age, {name}?\n')
    try:
        age = int(age)
        if age <= 0:
            print('The value is not correct, only positive numbers are allowed.')
            return validate_input_age(name)
        return age_validation(age, name)
    except ValueError:
        print('The value is not correct, only numbers are allowed.')
        return validate_input_age(name)

def evil_status(name):
    if (name == 'ben') or (name == 'pat'):
        if not barista.ask_yes_no('Are you evil?\n'):
            print('Oh, come on in!')
            return True
        good_deeds = int(input('How many good deeds have you done today?\n'))
        if good_deeds >= 4:
            print('All right, you can have a coffee.')
            return True
        print('No coffee for you!')
        return False
    return True
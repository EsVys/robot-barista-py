def greet(greeting: str):                                                             
    print(f'{greeting} Welcome to our coffee shop.')
    name = input('What is your name?\n')
    if not bool(name):
        name = 'Darling'

    return name

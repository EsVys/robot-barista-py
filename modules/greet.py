def greet(greeting: str):                                                             
    print(greeting + ' Welcome to our coffee shop.')

    name = input('What is your name?\n')
    if not bool(name):
        name = 'Darling'

    return name

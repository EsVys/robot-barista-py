import modules.greet as greet
import modules.bouncer as bouncer
import modules.barista as barista

def main():
    greeting = 'Hello!'
    name = greet.greet(greeting)
    age = bouncer.validate_input_age(name)
    bouncer.evil_status(name)
    barista.get_order(name)

if __name__ == "__main__":
    main()                                                  
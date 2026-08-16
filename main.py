import modules.greet as greet
import modules.bouncer as bouncer
import modules.barista as barista

def main():
    greeting = 'Hello!'
    while True:
        name = greet.greet(greeting)
        if name.lower() == 'david':
            barista.easter_egg_david(name)
            continue
        if not bouncer.validate_input_age(name):
            continue
        if not bouncer.evil_status(name):
            continue
        barista.get_order(name)

if __name__ == "__main__":
    main()
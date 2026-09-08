class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: ${self.price:.2f}'


class Coffee(MenuItem):
    def __init__(self, name: str, price: float, hot: bool = True):
        super().__init__(name, price)
        self.hot = hot

    def add_milk(self):
        milk = input('Do you wish to add oat milk?\n').lower()
        if milk == 'yes':
            self.price += 0.25
        elif milk == 'no':
            pass
        else:
            print('The value is not correct, please chose valid option.')
            self.add_milk()
        return self.price

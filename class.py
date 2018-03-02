class Calculator:
    name = 'Good calculator'
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.add(1,1)

    def add(self, x, y):
        print(x+y)
    def minus(self, x, y):
        print(x-y)
    
#c = Calculator('Bad calculator', 18)
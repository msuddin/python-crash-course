class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f'Make: {self.make}, Model: {self.model}, Year {self.year}'
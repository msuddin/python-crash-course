class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        print(f'Make is {self.make}, year is {self.year}')
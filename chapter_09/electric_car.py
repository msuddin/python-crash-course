class PaymentPlan:

    def __init__(self, country, code):
        self.country = country
        self.code = code

    def describe_payment_plan(self):
        return f'Payment plan: country: {self.country}, code: {self.code}'


class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        print(f'Make is {self.make}, year is {self.year}')


class ElectricCar(Car): # Inherits from Car class

    def __init__(self, make, year):
        super().__init__(make, year)
        self.hybrid = True
        self.paymentPlan = PaymentPlan('US', '001') # Using another class in this electric car

    def describe(self):
        print(f'Make is {self.make}, year is {self.year}, and the hybrid is {self.hybrid}')

    def is_hybrid(self):
        return self.hybrid

    def describe_payment(self):
        print(self.paymentPlan.describe_payment_plan())


my_car = ElectricCar('BMW', 2025)
my_car.describe() # Calls method from base class
print(f'Is {my_car.make} a hybride car: {my_car.is_hybrid()}') # Calling method from child class
my_car.describe_payment()
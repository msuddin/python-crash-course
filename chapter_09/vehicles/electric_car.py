from car import Car
from payment_plan import PaymentPlan

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
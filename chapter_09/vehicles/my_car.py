from electric_car import ElectricCar as e

my_car = e('BMW', 2025)
my_car.describe() # Calls method from base class
print(f'Is {my_car.make} a hybride car: {my_car.is_hybrid()}') # Calling method from child class
my_car.describe_payment()
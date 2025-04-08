from car import Car

def test_car():
    car = Car('bmw', 'hybrid', 1999)
    car_description = car.describe()
    assert car_description == 'Make: bmw, Model: hybrid, Year 1999'
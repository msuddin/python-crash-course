cars = ['honda', 'toyota', 'bmw', 'audi']
print(cars) # print list as is

cars.sort() # sort alphabetically
print(cars)

cars.sort(reverse=True) # sort reverse alphabetically
print(cars)

print(sorted(cars)) # using a temporary method to sort cars
print(cars)

cars.reverse() # sort reverse in order in list, not alphabetically reverse
print(cars)
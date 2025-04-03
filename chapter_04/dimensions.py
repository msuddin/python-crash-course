dimensions = (200, 20) # this is not a list but a tuple (using () instead of []), basically a constant list, the values can not change
print(dimensions)

for dimension in dimensions: # it is not possible to change the dimensions
    dimension = dimension * 2
    print(dimension)

print(dimensions)

dimensions = (400, 40) # but you can chance the values inside them
print(dimensions)
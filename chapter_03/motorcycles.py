motorcycles = ['honda', 'mitshubishi', 'civic', 'harley']
print(motorcycles)

motorcycles[0] = 'zonda' # changing the value of a list item
print(motorcycles)

motorcycles.append("batman's bike") # adding an item to the end of the list
print(motorcycles)

motorcycles.insert(-1, "robin's bike") # adding an item somewhere specific, this case second to last item
print(motorcycles)

motorcycles.pop() # removing last item from the list
print(motorcycles)

motorcycles.pop(0) # removing specific item from the list
print(motorcycles)
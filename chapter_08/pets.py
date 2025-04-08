def describe_pet(animal_type, pet_name, comment='none'): # default value
    """Display the information about a particular pet."""
    print(f"\nAnimal: {animal_type}")
    print(f"Pet name: {pet_name}")
    print(f"Any comments: {comment}.\n")

describe_pet('dog', 'fido')
describe_pet('cat', 'mitten')
describe_pet('godzilla', 'titan') # order matters

# can pass in keywords instead which means any order is ok
describe_pet(animal_type='titan', pet_name='godzilla')
describe_pet(pet_name='godzilla', animal_type='titan')

describe_pet('godzilla', 'titan', 'king of titans')
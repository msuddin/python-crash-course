def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        return f"Full Name: {first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"Full Name: {first_name.title()} {last_name.title()}"

person = get_full_name("john", "smith")
print(person)

person_2 = get_full_name("john", "smith", 'jay')
print(person_2)
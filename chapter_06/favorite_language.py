favorite_language = {
    'jimmy': 'python',
    'karl': 'c',
    'mandy': 'ruby',
    'andy': 'javascript',
}

print(f"The favorite language for Jimmy is {favorite_language['jimmy'].title()}.")

# What if what your trying to access does not exist, you can provide a default value
print(favorite_language.get('james', 'james does not exist in the list'))

friends = ['jimmy', 'karl']

for name in favorite_language.keys():
    if name in friends:
        print(f"I see that {name} language of choice is {favorite_language[name].title()}")

# You can sort dictionaries also
for name in sorted(favorite_language.keys()):
    print(name)

# You can also loop through the values only
for language in favorite_language.values():
    print(language)
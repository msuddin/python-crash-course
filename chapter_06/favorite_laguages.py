# Lists inside a dictionary

favorite_languages = {
    'sarah': ['python', 'c#'],
    'kate': 'java',
    'andy': ['python', 'ruby'],
}
print(favorite_languages)

for k, v in favorite_languages.items():
    print(k, v)
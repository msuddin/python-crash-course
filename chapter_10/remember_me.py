from pathlib import Path
import json

# Set the path to the file
path = Path('chapter_10/user.json')

# Load data into the file
user_name = input('Enter your name: ')
contents = json.dumps(user_name)
path.write_text(contents)

# Load data from the file
user_name = json.loads(path.read_text())
print(f'Hello {user_name}!')
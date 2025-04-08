from pathlib import Path

path = Path('chapter_10/names.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

while True:
    new_name = input('Enter new name (type quit to quit): ')
    if new_name == 'quit':
        break
    contents = new_name + '\n' + contents
    path.write_text(contents)
    contents = path.read_text()
    print(contents)
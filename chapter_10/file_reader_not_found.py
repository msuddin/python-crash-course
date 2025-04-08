from pathlib import Path

path = Path('names.txt')
try:
    contents = path.read_text()
    contents = contents.rstrip()
    print(contents)

except FileNotFoundError:
    print('File not found')




while True:
    new_name = input('Enter new name (type quit to quit): ')
    if new_name == 'quit':
        break
    contents = new_name + '\n' + contents
    path.write_text(contents)
    contents = path.read_text()
    print(contents)
from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = Path('chapter_10/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
from pathlib import Path    

filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
    print(f"Reading {filename}:")

    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:   
        print(contents)
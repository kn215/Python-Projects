from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
# contents = contents.replace('python', 'c')
# print(contents)

print(f"\nPrinting lines individually in for loop")
lines = contents.splitlines()

for line in lines:
    line = line.replace('python', 'C')
    print(line)


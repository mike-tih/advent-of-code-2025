def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result

total: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

rows = [line.split() for line in lines]

for column in zip(*rows):
    last = len(column) - 1
    if column[last] == "+":
        total += sum([int(x) for x in column[:last]])
    else:
        total += prod([int(x) for x in column[:last]])

print(f"Password is {total}")

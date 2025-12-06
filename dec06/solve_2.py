def prod(nums: list[int]):
    result = 1
    for x in nums:
        result *= x
    return result

total: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Split rows to identify column boundaries
rows_raw = [line.split() for line in lines]
columns_raw = [column for column in zip(*rows_raw)]
columns_maxdigits = [max([len(n) for n in column]) for column in columns_raw]
columns_count = len(columns_maxdigits)

# Column boundaries we will follow to keep spaces used for digits alignement
dividers = [sum(columns_maxdigits[:i]) + i for i in range(columns_count + 1)]

# Only here we have a matrix, where every element is an aligned number and len(num) is the same for the whole column
matrix = [[line[dividers[i]:dividers[i + 1] - 1] for i in range(columns_count)] for line in lines]

for column in zip(*matrix):
    last = len(column) - 1
    maxlen = max([len(x) for x in column[:last]])

    # Build numbers horizontally from top to bottom
    numbers = [int("".join([n[i] if n[i] != " " else "" for n in column[:last]])) for i in range(maxlen)]
    print(numbers)
    if column[last][0] == "+":
        total += sum(numbers)
    else:
        total += prod(numbers)

print(f"Password is {total}")
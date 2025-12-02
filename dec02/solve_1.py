counter: int = 0

with open('input.txt', 'r') as f:
    ranges: list[str] = f.read().split(',')

for r in ranges:
    start: int = int(r.split('-')[0])
    end: int = int(r.split('-')[1]) + 1

    for i in range(start, end):
        numlen: int = len((str(i)))
        if numlen % 2 == 1:
            continue
        else:
            halflen: int = numlen // 2
            if (str(i)[halflen:] == str(i)[:halflen]):
                print(f"{i}, ", end="")
                counter += i

print(f"\nPassword is {counter}")
SIZE = 12
total: int = 0

with open('input.txt', 'r') as f:
    banks: list[str] = f.read().splitlines()

for bank in banks:
    joltage_str: str = ""
    pos = 0
    for j in range(SIZE):
        jmax: int = 1
        for i in range(pos, len(bank) - SIZE + j + 1):
            if (int(bank[i]) > jmax):
                jmax = int(bank[i])
                pos = i
        joltage_str += bank[pos]
        pos += 1
    print(joltage_str)
    total += int(joltage_str)

print(f"\nPassword is {total}")
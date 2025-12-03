total: int = 0

with open('input.txt', 'r') as f:
    banks: list[str] = f.read().splitlines()

for bank in banks:
    maxpos = 0
    for i in range(1, len(bank) - 1):
        if (bank[i] > bank[maxpos]):
            maxpos = i
    secpos = maxpos + 1
    if (len(bank) - 1 > secpos):
        for i in range(maxpos + 2, len(bank)):
            if (bank[i] > bank[secpos]):
                secpos = i

    joltage = int(bank[maxpos] + bank[secpos])
    print(joltage)
    total += joltage

print(f"\nPassword is {total}")
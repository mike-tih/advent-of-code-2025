def is_in_ranges(n: int, ranges: list[tuple[int, int]]) -> bool:
    for r in ranges:
        if r[0] <= n <= r[1]:
            return True
    return False

ranges: list[tuple[int, int]] = []
counter: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

divider_passed: bool = False
for line in lines:
    if (line) == "":
        divider_passed = True
        continue
    if divider_passed:
        if is_in_ranges(int(line), ranges):
            counter += 1
    else:
        ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))

print(f"Password is {counter}")
ways: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

e_lines = [line for line in lines if line.find("^") >= 0]
max_depth = len(e_lines) - 1
start = lines[0].index("S")

cache = {}

def go_down(depth, pos) -> int:
    if depth > max_depth:
        return 1
    if (depth, pos) in cache:
        return cache[(depth, pos)]

    out: int = 0
    if e_lines[depth][pos] == ".":
        out = go_down(depth + 1, pos)
    elif e_lines[depth][pos] == "^":
        out = go_down(depth + 1, pos - 1) + go_down(depth + 1, pos + 1)
        
    cache[(depth, pos)] = out
    return out

ways = go_down(0, start)

print(f"Password is {ways}")
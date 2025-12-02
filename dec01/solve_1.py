def ft_spin(start_pos: int, moves: int) -> int:
    return (start_pos + moves) % 100

pos: int = 50
counter: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    moves = int(line[1:])
    if line[0] == "L":
        moves = -moves
    
    pos = ft_spin(pos, moves)
    print(f"Line: {line}, new position: {pos}")
    
    if pos == 0:
        counter += 1

print(f"Password is {counter}")
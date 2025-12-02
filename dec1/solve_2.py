def ft_spin(start_pos: int, moves: int) -> tuple[int, int]:
    new_pos = (start_pos + moves) % 100
    if moves > 0:
        passes = (start_pos + moves) // 100
    else:
        if start_pos == 0:
            remaining = abs(moves) - 1
            passes = remaining // 100
        else:
            steps_to_zero = start_pos
            if abs(moves) >= steps_to_zero:
                remaining = abs(moves) - steps_to_zero
                passes = 1 + remaining // 100
            else:
                passes = 0
    return (passes, new_pos)

pos: int = 50
counter: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    moves = int(line[1:])
    if line[0] == "L":
        moves = -moves
    
    passes, pos = ft_spin(pos, moves)
    counter += passes

    print(f"{line} -> {pos}: +{passes} = {counter}")

print(f"Password is {counter}")
splits: int = 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

beams = set()

for n, line in enumerate(lines):
    if n == 0:
        beams.add(line.index("S"))
        continue
    
    next_beams = set()
    
    for beam in beams:
        if line[beam] == "^":
            next_beams.add(beam + 1)
            next_beams.add(beam - 1)
            splits += 1
        else:
            next_beams.add(beam)
    
    beams = next_beams

print(f"Password is {splits}")
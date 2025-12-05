def get_neighbors(grid: list[str], row: int, col: int) -> list[str]:
    rows: int = len(grid)
    cols: int = len(grid[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1) 
    ]
    
    neighbors: list[str] = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append(grid[r][c])
    
    return neighbors

total: int = 0

with open('input.txt', 'r') as f:
    lines: list[str] = f.read().splitlines()

matrix: list[str] = [line for line in lines]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "@":
            if get_neighbors(matrix, i, j).count("@") < 4:
                print(f"x: {i}, y: {j}")
                total += 1

print(f"\nPassword is {total}")
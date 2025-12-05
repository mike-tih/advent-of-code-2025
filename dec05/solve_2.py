def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Объединяет пересекающиеся диапазоны"""
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))
    
    return merged

ranges: list[tuple[int, int]] = []

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    if line == "":
        break
    ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))

merged = merge_ranges(ranges)

total = sum(end - start + 1 for start, end in merged)

print(f"Password is {total}")
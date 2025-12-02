with open('input.txt', 'r') as f:
    ranges: list[str] = f.read().split(',')

counter: int = 0

for r in ranges:
    start: int = int(r.split('-')[0])
    end: int = int(r.split('-')[1]) + 1

    for i in range(start, end):
        numlen: int = len((str(i)))
        grouplen: int = 1
        while (grouplen <= numlen // 2):
            if (numlen % grouplen == 0):
                groupslen = numlen // grouplen 
                groups = [str(i)[j*grouplen:(j+1)*grouplen] for j in range(groupslen)]
                if all(group == groups[0] for group in groups):
                    print(f"{i}, ", end="")
                    counter += i
                    break
            grouplen += 1

print(f"\nPassword is {counter}")
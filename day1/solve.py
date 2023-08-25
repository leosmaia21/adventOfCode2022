elf = 0
max = 0
elfmeals = 0

total = []

with open("input.txt") as f:
    lines = f.readlines()
    print(lines)
    for i, line in enumerate(lines):
        if (line == "\n"):
            if (max < elfmeals):
                max = elfmeals
                elf = i
            total.append(elfmeals)
            elfmeals = 0
        else:
            elfmeals += int(line)
if (max < elfmeals):
    max = elfmeals
    total.append(max)

total.sort(reverse=True)
print("elf", elf, "max", max)
print("sum 3:", total[0] + total[1] + total[2])

        
            





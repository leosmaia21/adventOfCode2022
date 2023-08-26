
data = []
total = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        x = line.split()[0]
        y = []
        l = int(len(x))
        y.append(x[:int((l/2))])
        y.append(x[int((l/2)):])
        assert len(y[0]) == len(y[1])
        data.append(y)


for x in data:
    a = list(set(x[0]) & set(x[1]))
    if len(a) == 0:
        print("boas")
    a = ord(a[0])
    if a >= ord('a') and a <= ord('z'):
        total += a - ord('a') + 1
    if a >= ord('A') and a <= ord('Z'):
        total += a - ord('A') + 27
print(total)

#part2
total = 0
for i, x in enumerate(data):
    aux = i % 3

    if aux != 0:
        continue
    x0 = data[i + 0][0] + data[i + 0][1]
    x1 = data[i + 1][0] + data[i + 1][1]
    x2 = data[i + 2][0] + data[i + 2][1]
    a = list(set(x0) & set(x1) & set(x2))
    a = ord(a[0])
    if a >= ord('a') and a <= ord('z'):
        total += a - ord('a') + 1
    if a >= ord('A') and a <= ord('Z'):
        total += a - ord('A') + 27
    
print(total)




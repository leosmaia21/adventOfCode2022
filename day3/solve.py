
data = []
with open("input2.txt") as f:
    lines = f.readlines()
    for line in lines:
        x = line.split()[0]
        y = []
        l = int(len(x))
        y.append(x[:int((l/2))-1])
        y.append(x[int((l/2)):])
        data.append(y)


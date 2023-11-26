

datafile = "data.txt"
datafile = "test.txt"
# data = [[0 for j in range(8)] for i in range(10)]
data = [[] for _ in range(4)]
instructions = []

with open(datafile) as file:
  for index, line in enumerate(file):
    if line[:4] != 'move':
      for i, c in enumerate(line):
        if c.isalpha():
          print(c, i//4 + 1)
          data[i//4 + 1].append(c)
    else:
      ins = line.split()
      instructions.append((int(ins[1]), int(ins[3]), int(ins[5])))

for ins in instructions:
  x = data[ins[1]][:ins[0]]
  data[ins[1]] = data[ins[1]][ins[0] - 1:]
  data[ins[2]] = x + data[ins[2]]
  print(data)



datafile = "data.txt"
# datafile = "test.txt"
data = [[] for _ in range(10)]
instructions = []
with open(datafile) as file:
  for index, line in enumerate(file):
    if line[:4] != 'move':
      for i, c in enumerate(line):
        if c.isalpha():
          data[i//4 + 1].append(c)
    else:
      instructions.append([int(ins) for i, ins in enumerate(line.split()) if i % 2 !=0])

for i, ins in enumerate(instructions):
  quantity, src, dst = ins[0], ins[1], ins[2]
  x = data[src][:quantity][::-1]
  data[src] = data[src][quantity:]
  data[dst] = x + data[dst]

for d in data[1:]:
  print(d[0])

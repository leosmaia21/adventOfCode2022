




dados = {}

file = "teste.txt"
file = "data.txt"
data = []

out = []

index = 0

f = open(file)

def goFolder(name):
  ret = 0
  global index
  while True:
    cmd = f.readline()[:-1].split()
    if len(cmd) == 0:
      break
    if cmd[0].isdigit():
      ret += int(cmd[0])
    elif len(cmd) > 2 and cmd[1] == "cd" and cmd[2] != "..":
      if (len(name) != 0 and name[-1] != "/"):
        name = name+"/"
      value = goFolder(name+cmd[2])
      out.append([name+cmd[2], value])
      ret += value
    elif len(cmd) == 3 and cmd[2] == "..":
      return ret
  return ret

goFolder("")
# print(out)

final = 0;
for folder in out:
  if folder[1] <= 100000:
    final += folder[1]

numero = 30000000 - (70000000 - 40389918)

filtered = list(filter(lambda x: x[1] >= numero, out))

filtered = min(filtered, key=lambda x: x[1])

print(filtered)



dados = []


file = "dados.txt"
with open(file) as f:
  dados = [[int(x) for x in line[:-1]] for line in f]



total = len(dados) * len(dados[0])

for index in range(total):
  x = index % len(dados[0])
  y = index // len(dados[0])

  for hor in range(len(dados[0])):


print(dados)

#! /bin/python3

def isinrange(inicial, end, x):
  return 1 if int(x) >= int(inicial) and int(x) <= int(end) else 0


# with open('teste.txt', 'r') as f:
#   lines = f.readlines()
#   assignment_pairs = [entry.strip() for entry in lines]
#   data = [x.split(",") for x in assignment_pairs]
#   data = [[x[0].split("-"), x[1].split("-")] for x in data]
#   ret = 0
#   for entry in data:
#     if isinrange(entry[0][0], entry[0][1], entry[1][0]) and isinrange(entry[0][0], entry[0][1], entry[1][1]):
#       ret += 1
#     elif isinrange(entry[1][0], entry[1][1], entry[0][0]) and isinrange(entry[1][0], entry[1][1], entry[0][1]):
#       ret += 1
      

  # print(ret)
  

#part 2

 
with open('data.txt', 'r') as f:
  lines = f.readlines()
  assignment_pairs = [entry.strip() for entry in lines]
  data = [x.split(",") for x in assignment_pairs]
  data = [[x[0].split("-"), x[1].split("-")] for x in data]

  ret = 0
  for entry in data:
    if isinrange(entry[0][0], entry[0][1], entry[1][0]) or isinrange(entry[0][0], entry[0][1], entry[1][1]):
      ret += 1
    elif isinrange(entry[1][0], entry[1][1], entry[0][0]) or isinrange(entry[1][0], entry[1][1], entry[0][1]):
      ret += 1
      

  print(ret)

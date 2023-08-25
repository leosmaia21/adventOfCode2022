

#part 1
data = []
rounds = 0
with open("input2.txt") as f:
    lines = f.readlines()
    for line in lines:
        x = line.split()
        data.append(x)
score = 0
rounds = len(data)
for i in range(rounds):
    mine = ord(data[i][1])
    enemy = ord(data[i][0]) - ord('A')
    mineShiffet = mine - ord('X')
    ret = enemy - mineShiffet
    if ret == 0:
        score += mineShiffet + 1 + 3
    elif (enemy - 1) % 3 == mineShiffet:
        score += mineShiffet + 1
    elif (enemy + 1) % 3 == mineShiffet:
        score += mineShiffet + 1 + 6


print("score", score)

#part 2

data = []
rounds = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        x = line.split()
        data.append(x)
score = 0
rounds = len(data)
for i in range(rounds):
    mine = ord(data[i][1])
    enemy = ord(data[i][0]) - ord('A')
    goal = mine - ord('X')

    if goal == 0:
        score += (enemy - 1) % 3 + 1
    elif goal == 1:
        score += enemy + 1 + 3
    elif goal == 2:
        score += (enemy + 1) % 3 + 1 + 6

print("score", score)
    



file = "data.txt"

with open(file) as f:
  data = f.readline()
  # data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
  # data= "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
  # data ="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

  for i in range(0, len(data) -14):
    x = list(data[i: i+14])
    print(x)
    if len(set(x)) == 14:
      print(x, i + 13 + 1)
      break


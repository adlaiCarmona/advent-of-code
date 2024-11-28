file = open("sample.txt","r")

input = [line.strip() for line in file]
possible_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def multiply_list(l:list):
  result = 1
  for i in l:
    result *= i
  return result

def puzzle1():
  hands = [i.split(" ")[0] for i in input]
  bets = [[*map(int, i.split(" ")[1])] for i in input]
  
  # print(hands)
  # print(bets)

  result = 0
  for index, hand in enumerate(hands):
    if hand[] == "rock":
      if bets[hand[0]][0] == 1:
        result += bets[hand[0]][1]

  # for i in range(0, len(times)):
  #   win_options.append(len(get_win_options(times[i], distance_records[i])))

  # result = multiply_list(win_options)
  return None

def puzzle2():
  times = [*map(int, input[0].split(": ")[1].replace(" ","").split())]
  distance_records = [*map(int, input[1].split(": ")[1].replace(" ","").split())]

  print(times)
  print(distance_records)

  win_options = []

  for i in range(0, len(times)):
    win_options.append(len(get_win_options(times[i], distance_records[i])))

  result = multiply_list(win_options)
  return result

print(puzzle1())
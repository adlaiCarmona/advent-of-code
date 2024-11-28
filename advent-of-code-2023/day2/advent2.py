file = open("input.txt","r")

def puzzle1():
  posible_games = []

  in_bag = {
    "red": 12,
    "green": 13,
    "blue": 14
  }

  for line in file:
    data = line.replace("\n","").split(":")
    print(data)
    rounds = data[1].split(";")

    is_possible = True

    for round in rounds:
      if is_possible == False:
        break
      items = round.split(",")
      for item in items:
        value = item.strip().split(" ")[0]
        print(value)
        if "red" in item:
          if int(value) > in_bag["red"]:
            is_possible = False
            break
        if "green" in item:
          if int(value) > in_bag["green"]:
            is_possible = False
            break
        if "blue" in item:
          if int(value) > in_bag["blue"]:
            is_possible = False
            break
    if is_possible:
      posible_games.append(int(data[0].replace("Game ","")))


  print("The posible games are = {}; sum of the ids = {}".format( posible_games, sum(posible_games) ))

def puzzle2():
  power_cubes = []

  for line in file:
    minimum = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    
    data = line.replace("\n","").split(":")
    print(data)
    rounds = data[1].split(";")

    for round in rounds:
      items = round.split(",")
      for item in items:
        value = int(item.strip().split(" ")[0])
        print("item = '{}'; value = {}".format(item, value))
        if "red" in item:
          if value > minimum["red"]:
            minimum["red"] = value
        if "green" in item:
          if value > minimum["green"]:
            minimum["green"] = value
        if "blue" in item:
          if value > minimum["blue"]:
            minimum["blue"] = value
    
    print(minimum)
    power_cubes.append(minimum["red"] * minimum["green"] * minimum["blue"])

  print("The power of cubes are = {};\n adding it up = {}".format( power_cubes, sum(power_cubes) ))

puzzle2()
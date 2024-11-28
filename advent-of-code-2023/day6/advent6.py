file = open("input.txt","r")

input = [line.strip() for line in file]

def multiply_list(l:list):
  result = 1
  for i in l:
    result *= i
  return result

def get_win_options(race_time, distance_record):
  win_options = []
  for time_pressed in range(1, race_time):
    speed = time_pressed
    remaining_time = race_time - time_pressed
    distance = speed * remaining_time
    if distance > distance_record:
      win_options.append(time_pressed)
  return win_options

def puzzle1():
  times = [*map(int, input[0].split(": ")[1].split())]
  distance_records = [*map(int, input[1].split(": ")[1].split())]

  print(times)
  print(distance_records)

  win_options = []

  for i in range(0, len(times)):
    win_options.append(len(get_win_options(times[i], distance_records[i])))

  result = multiply_list(win_options)
  return result

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

print(puzzle2())
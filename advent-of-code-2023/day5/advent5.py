file = open("input.txt","r")

input_info = []
maps = []

def get_seeds_puzzle2(l:list):
  seeds = []
  for seed_range in range(int(len(l)/2)):
    index = seed_range * 2
    # print(l[index], l[index + 1])
    # print(range(l[index], l[index]+l[index + 1]))
    # print(list(range(l[index], l[index + 1])))
    # seeds.append(list(range(l[index], l[index + 1])))
    seeds.extend(range(l[index], l[index]+l[index + 1] + 1))
  print(seeds)
  return seeds

def load_input():
  category = None
  for line in file:
    if line == "\n":
      input_info.append(category)
      category = []
      continue

    if category == None:
      # seeds = list(map(lambda x: int(x), line.replace("\n","").split(":")[1].strip().split(" ")))
      category = list(map(lambda x: int(x), line.replace("\n","").split(":")[1].strip().split(" ")))
      # print(s)
      # category = get_seeds_puzzle2(s)
      continue

    if not ":" in line:
      category.append(list(map(lambda x: int(x), line.replace("\n","").split(" "))))
  input_info.append(category)

def setup_maps():
  for map in range(1, len(input_info)):
    dictionary = {}
    for record in range(0, len(input_info[map])):
      for number in range(0, input_info[map][record][2]):
        dictionary[input_info[map][record][1] + number] = input_info[map][record][0] + number
    maps.append(dictionary)

def using_dict():
  locations = []

  for seed in input_info[0]:
    value = seed
    # print("Seed {}".format(seed))
    for map in maps:
      if value not in map:
        # print("Value {} not in map".format(value))
        continue
      # print("Map {}".format(map))
      # print("Mapping {}: {}".format(value, map[value]))
      value = map[value]
    locations.append(value)

def setup_maps():
  for map in range(1, len(input_info)):
    dictionary = {}
    for record in range(0, len(input_info[map])):
      for number in range(0, input_info[map][record][2]):
        dictionary[input_info[map][record][1] + number] = input_info[map][record][0] + number
    maps.append(dictionary)

def get_map_value(map, value):
  destination_value = map[0]
  source_value = map[1]
  map_length = map[2]
  if source_value <= value and value <= source_value + map_length:
    return destination_value + (value - source_value)
  return None

def puzzle1():
  load_input()
  # setup_maps()
  print(input_info)
  # print(maps)

  locations = []
  lowest_location = None

  seeds = input_info[0]
  print("Seeds = {}".format(seeds))

  for seed_index in range(0, len(seeds), 2):
    value = seeds[seed_index]
    seeds_length = seeds[seed_index + 1]
    reduced_seeds = []

    reduced_seeds.append(value)
    while reduced_seeds:

      # print("Seed {}".format(seed))
      for maps in input_info[1:]:
        found = False
        for map in maps:
          # print("\tMap {}".format(map))
          # print("Mapping {}: {}".format(value, map[value]))
          if not found:
            new_value = get_map_value(map, value)
            if new_value != None:
              # print("\t\tMap value {}: {}; Map = {}".format(value, new_value, map))
              value = new_value
              found = True
      if lowest_location == None or value < lowest_location:
        lowest_location = value
    # locations.append(value)
  
  print("Lowest location {}".format( lowest_location ))
  # print("All locations = {};\n lowest location {}".format( locations, min(locations) ))

def puzzle2():
  load_input()
  print(input_info)

  locations = []
  lowest_location = None

  seeds = []
  print("Seeds = {}".format(seeds))

  for seed_index in range(0, len(input_info[0]), 2):
    seed_start = seeds[seed_index]
    seeds_length = seeds[seed_index + 1]

    left = []

    reduced_seeds.append(value)
    while reduced_seeds:
       return 0

  for seed in seeds:
    value = seeds[seed_index]
      
    # print("Seed {}".format(seed))
    for maps in input_info[1:]:
      found = False
      for map in maps:
        # print("\tMap {}".format(map))
        # print("Mapping {}: {}".format(value, map[value]))
        if not found:
          new_value = get_map_value(map, value)
          if new_value != None:
            # print("\t\tMap value {}: {}; Map = {}".format(value, new_value, map))
            value = new_value
            found = True
    if lowest_location == None or value < lowest_location:
      lowest_location = value
    # locations.append(value)
  
  print("Lowest location {}".format( lowest_location ))
  # print("All locations = {};\n lowest location {}".format( locations, min(locations) ))

def get_test_input(day_num, is_raw):
        inputs = [line.strip("\n") if is_raw else line.strip() for line in open("input.txt", "r").readlines()]
        return inputs

def part2(data):
        seeds = [*map(int, data[0].split(": ")[1].split())]
        maps = [[[*map(int, n.split())] for n in i.split("\n")[1:]] for i in "\n".join(data[2:]).split("\n\n")]

        locations = []
        seed_pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
        for pair in seed_pairs:
            remain = [pair]
            result = []

            for _map in maps:
                while remain:
                    cur = remain.pop()  # cur = x-y
                    for dest, src, rng in _map:  # src-(src+rng-1) = a-b
                        if cur[1] < src or src + rng <= cur[0]:  # no overlap, x-y-a-b or a-b-x-y
                            continue
                        elif src <= cur[0] <= cur[1] < src + rng:  # a-x-y-b
                            offset = cur[0] - src
                            result.append((dest + offset, dest + offset + cur[1] - cur[0]))
                            break
                        elif cur[0] < src <= cur[1] < src + rng:  # x-a-y-b
                            offset = cur[1] - src
                            result.append((dest, dest + offset))
                            remain.append((cur[0], src - 1))
                            break
                        elif src <= cur[0] < src + rng <= cur[1]:  # a-x-b-y
                            offset = cur[0] - src
                            result.append((dest + offset, dest + rng - 1))
                            remain.append((src + rng, cur[1]))
                            break
                        elif cur[0] < src <= src + rng <= cur[1]:  # x-a-b-y
                            result.append((dest, dest + rng - 1))
                            remain.append((cur[0], src - 1))
                            remain.append((src + rng, cur[1]))
                            break
                    else:  # didn't match any source range
                        result.append(cur)
                remain = result
                result = []
            locations.extend(remain)

        # print(locations)
        return min(i[0] for i in locations)

# print(get_test_input(5, False))
print(part2(get_test_input(5, False)))
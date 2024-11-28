file = open("input.txt","r")

matrix = []
matrix = [ line.replace("\n","") for line in file]

def get_value_safe(row, column):
  if row < 0 or row >= len(matrix):
    return "x"
  if column < 0 or column >= len(matrix[row]):
    return "x"
  return matrix[row][column]

def get_num_from_adjacent(row, column):
  num = {
    "value": None,
    "start": None,
    "end": None,
  }

  start = column
  while matrix[row][start].isdigit():
    if start == 0:
      break
    if matrix[row][start - 1].isdigit():
      start -= 1
    else:
      break

  end = column
  while matrix[row][end].isdigit():
    if end == len(matrix[row]) - 1:
      break
    if matrix[row][end + 1].isdigit():
      end += 1
    else:
      break
    
  num["start"] = start
  num["value"] = get_num_in_matrix(row, start)
  num["end"] = end

  return num

def check_adjacent_for_number(row, column):
  adjacent = {
    "first": None,
    "second": None,
    "start_first": None,
    "start_second": None,
    "end_first": None,
    "end_second": None,
  }
  num_of_adjacent = 0
  if row == 46 and column == 47:
        print("{} {}".format(range(row - 1, row + 2), range(column - 1, column + 2)))
  for j in range(row - 1, row + 2):
    new_adjacent_end = None
    for i in range(column - 1, column + 2):
      if new_adjacent_end != None and i <= new_adjacent_end:
        continue
      value = get_value_safe(j,i)
      if row == 46 and column == 47:
        print("{} {} {}".format(value, j, i))
      if value.isdigit():
        if row < 50:
          print("\t\t\t{} {} {}".format(value, j, i))
        num_of_adjacent += 1
        adjacent_info = get_num_from_adjacent(j, i)
        if j < 50:
          print(adjacent_info)
        new_adjacent_end = adjacent_info["end"]
        
        if adjacent["first"] == None:
          adjacent["first"] = adjacent_info["value"][0]
          adjacent["start_first"] = adjacent_info["start"]
          adjacent["end_first"] = adjacent_info["end"]
        elif adjacent["second"] == None:
          adjacent["second"] = adjacent_info["value"][0]
          adjacent["start_second"] = adjacent_info["start"]
          adjacent["end_second"] = adjacent_info["end"]
      # 74722047
      
  if num_of_adjacent == 2:
    return adjacent
  return None

def check_for_symbol_in_line(row, start, end):
  if row < 0 or row >= len(matrix):
    return False
  
  for i in range(start, end + 1):
    if i < 0 or i >= len(matrix[row]):
      continue

    char = matrix[row][i]
    print("char = {}; i = {}; j = {};".format(char, i, row))
    if char != "." and not char.isdigit():
      print("\tis symbol")
      return True
  return False

def get_num_in_matrix(row, column):
  number = 0
  if row < 50:
    print("matrix[row][column]={}; row={}; column={}".format(matrix[row][column],row,column))
  while matrix[row][column].isdigit():
    # print(matrix[row][column])
    number *= 10
    number += int(matrix[row][column])
    column += 1
    if column >= len(matrix[row]):
      break
  return [number, column]

def puzzle1():
  part_number = []

  for nrow, row in enumerate(matrix):
    print(row)
    for ncolumn, column in enumerate(matrix[nrow]):
      print("\t{}".format(column))
      if column.isdigit() and not get_value_safe(nrow,ncolumn - 1).isdigit():
        print("\t\t{} {} {}".format(column, nrow, ncolumn))
        number_n_end = get_num_in_matrix(ncolumn, nrow)
        number = number_n_end[0]
        end = number_n_end[1]
        print("\t\t\t{} {}".format(number, end))
        is_valid = False
        for j in range(nrow - 1, nrow + 2):
          print("\t\t{} {} {}".format(j, ncolumn - 1, end + 1))
          is_valid = is_valid or check_for_symbol_in_line(j, ncolumn - 1, end)
        if is_valid:
          part_number.append(number)

  print("The part numbers are = {};\n sum of parts = {}".format( part_number, sum(part_number) ))

def puzzle2():
  gears = []

  for nrow, row in enumerate(matrix):
    # print(row)
    for ncolumn, column in enumerate(matrix[nrow]):
      # print("\t{}".format(column))
      if column == "*":
        print("\t\t{} {} {}".format(column, nrow, ncolumn))
        adjacent = check_adjacent_for_number(nrow, ncolumn)
        if nrow < 50:
          print(adjacent)
        if adjacent != None:
          # print("\t\t\t\t{} {}".format(adjacent["first"], adjacent["second"]))
          multiplication = adjacent["first"] * adjacent["second"]
          gears.append(multiplication)
        else:
          for j in range(nrow - 1, nrow + 2):
            print("\t\t\t\t\t{} {} {}".format(matrix[j][ncolumn - 1], matrix[j][ncolumn], matrix[j][ncolumn + 1]))

  print("The gears are = {};\n sum of gears = {}".format( gears, sum(gears) ))

puzzle2()
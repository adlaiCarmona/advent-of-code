file = open("input2.txt","r")

addition = 0

spelledout = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

for line in file:
  first = None
  last = None

  for [key, value] in spelledout.items():
    line = line.replace(key,key[0] + value + key[-1])

  for index in range(0, len(line)):
    if line[index].isdigit():
      if first == None:
        first = int(line[index])
      last = int(line[index])
  print("First = {}, Last = {}".format(first, last))
  addition += first * 10 + last

print("The sum of first and last digit = {}".format( addition ))
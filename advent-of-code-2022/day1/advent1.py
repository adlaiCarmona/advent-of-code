file = open("input.txt","r")

addition = 0
max = 0
leaderboard = [0, 0, 0]

index_current = 1
index_max = 0

for line in file:
  if line == "\n":
    minimum = min(leaderboard)
    if addition > minimum:
      index_minimum = leaderboard.index(minimum)
      leaderboard[index_minimum] = addition
      #max = sum
      #index_max = index_current
    addition = 0
    index_current += 1
    continue
  addition += int(line)

print("The sum of top 3 highest calorie elves = {}".format( sum(leaderboard) ))
#print("# of Elf with highest calories = {}\nNumber of max calories = {}".format(index_max, max))
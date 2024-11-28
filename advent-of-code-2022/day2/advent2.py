#
# A, X -> Rock 
# B, Y -> Paper
# C, Z -> Scissors
#

## win
# A, Y -> 0, 1
# B, Z -> 1, 2
# C, X -> 2, 0

file = open("input.txt","r")

points = 0
points_round = 1

# for line in file:
#   enemy_ord = ord(line[0]) - ord("A")
#   mine_ord = ord(line[2]) - ord("X")

#   # point depending what you choose
#   points_round += mine_ord

#   enemy_vs_mine = enemy_ord - mine_ord

#   # points depending if you tie
#   if( enemy_vs_mine == 0):
#     points_round += 3
#   elif( enemy_vs_mine == -1 or enemy_vs_mine == 2 ):
#     points_round += 6

#   print("Points per round = {}".format(points_round))
  
#   points += points_round
#   points_round = 1 # is the minimum score

# print("The total amount of points = {}".format( points ))

###########################################################

# Part two

#
# A -> Rock     -> 1
# B -> Paper    -> 2
# C -> Scissors -> 3
#
# X -> Lose   -> prev
# Y -> Draw   -> same
# Z -> Win    -> next

for line in file:
  enemy_ord = ord(line[0]) - ord("A")
  result_ord = ord(line[2]) - ord("X")

  # point depending result
  points_round += result_ord * 3

  if( result_ord == 1 ): # draw
    points_round += enemy_ord
  elif( result_ord == 2): # win
    if( enemy_ord != 2):
      points_round += enemy_ord + 1
  else: # lose
    if( enemy_ord == 0):
      points_round += 2
    else:
      points_round += enemy_ord - 1


  print("Points per round = {}".format(points_round))
  
  points += points_round
  points_round = 1 # is the minimum score

print("The total amount of points = {}".format( points ))
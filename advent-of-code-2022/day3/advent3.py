def get_priority(letter):
  if(letter.isupper()):
    return ord(letter) - 38
    # return ord(letter) - ord('A') + 27
  else:
    return ord(letter) - 96
    # return ord(letter) - ord('a') + 1

def get_in_both(array):
  half = len(array)//2
  left = array[:half]
  right = array[half:]
  
  for char in left:
    if(right.find(char) != -1):
      return char

file = open("sample.txt","r")

# in_both_compartments = []

# for line in file:
#   both = get_in_both(line)
#   both_priority = get_priority(both)

#   in_both_compartments.append(both_priority)

#   print("Item type to appear in both is: {} with prioritiy of: {}".format(both, both_priority))

# print("The total amount of priorities = {}".format( sum(in_both_compartments) ))

###########################################################

# Part two

in_both_compartments = []
in_badges = []

team = {0:None,1:None,2:None}
team_number = 0

for line in file:
  team[team_number] = set(line)

  team_number += 1
  if(team_number == 3):
    
    team_number = 0

  #in_both_compartments.append(both_priority)

  #print("Item type to appear in both is: {} with prioritiy of: {}".format(both, both_priority))

print("The total amount of priorities = {}".format( sum(in_both_compartments) ))
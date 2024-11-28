file = open("input.txt","r")

cards = [ line.replace("\n","") for line in file]

def get_nums_from_card_side(side: str):
  numbers = side.strip().replace("  "," ").split(" ")
  return [ int(number) for number in numbers ]

def add_copies_to_list(list: list, index: int, number: int, copies: int):
  print("index = {}\tnumber = {}".format(index, number))
  for i in range(index, index + number):
    list[i] += copies

def puzzle1():
  total_points = 0

  for index, card in enumerate(cards):
    print("Card {}:".format(index))
    card_points = 0

    numbers = card.split(":")[1].strip()
    numbers = numbers.split("|")
    numbers[0] = numbers[0].strip()
    numbers[1] = numbers[1].strip()
    # print(numbers)
    winning_numbers = get_nums_from_card_side(numbers[0])
    card_numbers = get_nums_from_card_side(numbers[1])

    print(winning_numbers)
    print(card_numbers)

    for number in card_numbers:
      if number in winning_numbers:
        if card_points == 0:
          card_points += 1
        else:
          card_points *= 2
    print("Card points = {}".format( card_points ))
    total_points += card_points

  print("The total points = {}".format( total_points ))


def puzzle2():
  total_scratch_cards = [ 1 for _ in cards ]

  for index, card in enumerate(cards):
    print("Card {}:".format(index))
    card_points = 0

    numbers = card.split(":")[1].strip()
    numbers = numbers.split("|")
    numbers[0] = numbers[0].strip()
    numbers[1] = numbers[1].strip()
    # print(numbers)
    winning_numbers = get_nums_from_card_side(numbers[0])
    card_numbers = get_nums_from_card_side(numbers[1])

    print(winning_numbers)
    print(card_numbers)

    for number in card_numbers:
      if number in winning_numbers:
        card_points += 1
    add_copies_to_list(total_scratch_cards, index + 1, card_points, total_scratch_cards[index])
    print("Card points = {}".format( card_points ))
    print(total_scratch_cards)
    print("The total of scratch cards = {}\t at {}".format( sum(total_scratch_cards), index ))

  print("The total of scratch cards = {}".format( sum(total_scratch_cards) ))

puzzle2()
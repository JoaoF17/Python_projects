import random

cards = ["A", "K", "J", "Q", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

card_points = {
  "A" : 11 or 1,
  "K" : 10,
  "J" : 10,
  "Q" : 10,
  "10" : 10,
  "9" : 9,
  "8" : 8,
  "7" : 7,
  "6" : 6,
  "5" : 5,
  "4" : 4,
  "3" : 3,
  "2" : 2,
}

#create a random number within a number of cards, so it can be used to pull a random card
def random_number():
  r = random.randint(0, len(cards)-1)
  return r

#player hand, 2 random cards
p1 = random_number()
p2 = random_number()
player = [cards[p1], cards[p2]]

#logic to count points
player_points = 0
for point in player:
  single_card_points = card_points[point]
  player_points += single_card_points

#dealer hand, 1 random card, and a facing down card
d1 = random_number()
dealer = [cards[d1], "_"]

#logic to count points for computer
computer_points = 0
for point in dealer:
  if point == "_":
    single_card_points = 0
  else:
    single_card_points = card_points[point]
  computer_points += single_card_points

#function for player to draw a card
def draw_card():
  player.append(cards[random_number()])


print(f"Your hand: {player} Points: {player_points}")
print(f"Dealer hand: {dealer} Points: {computer_points}")
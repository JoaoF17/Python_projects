import random

cards = ["A", "K", "J", "Q", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

card_points = {
  "A" : 11,
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

#player hand, 2 random cards and points
p1 = random_number()
p2 = random_number()
player = [cards[p1], cards[p2]]

#dealer hand, 1 random card, and a facing down card
d1 = random_number()
dealer = [cards[d1]]

#functions for player and computer to draw a card
def player_draw_card():
  player.append(cards[random_number()])

def dealer_draw_card():
  dealer.append(cards[random_number()])

game_on = True
while game_on:
  #logic to count points for player
  player_points = 0
  for point in player:
    single_card_points = card_points[point]
    player_points += single_card_points
    
  #logic to count points for dealer
  dealer_points = 0
  for point in dealer:
    single_card_points = card_points[point]
    dealer_points += single_card_points
    
  print(f"Your hand: {player} Points: {player_points}")
  print(f"Dealer hand: {dealer} Points: {dealer_points}")
  
  player_prompt = input("Would you like to draw a card? 'Y' or 'N' \n").lower()
  
  if player_prompt == "y":
    player_draw_card()
    #recalculate points to make sure it's not over 21
    for point in player:
      single_card_points = card_points[point]
      player_points += single_card_points
    if player_points > 21:
      print("You went over, you lost.")
      game_on = False
      
  elif player_prompt == "n":
    while dealer_points < 17:
      dealer_draw_card()
      for point in dealer:
        single_card_points = card_points[point]
        dealer_points += single_card_points
      if dealer_points > 21:
        print("Dealer went over, YOU WON!")
      elif dealer_points > player_points:
        print("Dealer won!")
        game_on = False
  elif dealer_points > player_points:
    print("Dealer won!")
  
  print(f"Your hand: {player} Points: {player_points}")
  print(f"Dealer hand: {dealer} Points: {dealer_points}")
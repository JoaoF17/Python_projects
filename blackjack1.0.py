import random
from os import system

#function to deal cards
def deal_card():
  """Returns a random card from the deck

  Returns:
      int: card value
  """  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Calculate the score of each hand
def calculate_score(cards):
  """Calculates the score of each hand
  """  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1) 
  
  return sum(cards)

def compare(user_score, dealer_score):
  if user_score == dealer_score:
    return "It is a draw"
  elif user_score == 0:
    return "You won with a Blackjack"
  elif dealer_score == 0:
    return "Dealer won with a BlackJack"
  elif user_score > 21:
    return "You went over! Dealer wins."
  elif dealer_score > 21:
    return "Dealer went over! you win."
  elif user_score > dealer_score:
    return "You have more points than dealer! You won!"
  else:
    return "The dealer score higher! Dealer won!"

def play_game():
  user_cards = []
  dealer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())


  while not game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer cards: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_over = True
    else:
      deal_a_card = input("Type 'Y' to get another card, type 'N' to pass:\n").lower()
      if deal_a_card == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"your final hand is {user_cards} and the score is {user_score}")
  print(f"the dealer final hand is {dealer_cards} and the score is {dealer_score}")
  print(compare(user_score, dealer_score))

game_active = True
while game_active:
  if input("Do you wan't to play a game of BlackJack? Answer with 'Y' or 'N'\n").lower() == 'y':
    system("clear")
    play_game()
  else:
    game_active = False
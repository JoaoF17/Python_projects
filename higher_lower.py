from art import higher_lower_logo, vs
from higher_lower_data import data
from random import randint

def random_number():
  return randint(0, len(data)-1)

# a = data[random_number()]
# value = a['follower_count']
# print(value)

points = 0
game_on =  True

while game_on:
  a = data[random_number()]
  b = data[random_number()]
  player_answer = input(f"Who has more followers, option 'a' {a['name']} or option 'b' {b['name']}? Write 'a' or 'b'\n").lower()
  
  if player_answer == 'a' and a['follower_count'] > b['follower_count']:
    points += 1
    print(f"Correct! {a['name']} has more followers with {a['follower_count']} while {b['name']} has {b['follower_count']} followers.")
    print(f"Score: {points}")
  elif player_answer == 'b' and b['follower_count'] > a['follower_count']:
    points += 1
    print(f"Correct! {b['name']} has more followers with {b['follower_count']} while {a['name']} has {a['follower_count']} followers.")
    print(f"Score: {points}")
  else:
    print(f"Wrong!\n {a['name']} -> {a['follower_count']}\n {b['name']} -> {b['follower_count']} ")
    if input("Would you like to play again? 'Y' or 'N'?").lower() == 'y':
      points = 0
    else:
      game_on = False
    
    
  # print(f"{a['name']} -> {a['follower_count']}")
  # print(f"{b['name']} -> {b['follower_count']}")

  # if a['follower_count'] > b['follower_count']:
  #   print(f"{a['name']} has more followers with {a['follower_count']}")
  # else:
  #   print(f"{b['name']} has more followers with {b['follower_count']}")

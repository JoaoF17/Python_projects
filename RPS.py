import random

scissors = '''
   _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''

rock = '''
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

game_images = [rock, paper, scissors]

player_input = int(input("Type 0 for rock, 1 for paper and 2 for scissors. \n"))

print(f"Player: {game_images[player_input]}")
# if player_input == 0:
#   print("Player: " + rock)
# elif player_input == 1:
#   print("Player: " + paper)
# else:
#   print("Player: " + scissors)

random_number = random.randint(0,2)

print(f"Computer: {game_images[random_number]}")
# if random_number == 0:
#   print("Computer: " + rock)
# elif random_number == 1:
#   print("Computer: " + paper)
# else:
#   print("Computer: " + scissors)

if player_input == 0 and random_number == 2:
  print("Player Wins!")
elif random_number > player_input:
  print("Computer Wins!")
elif random_number == 0 and player_input == 2:
  print("Computer Wins!")
elif player_input == random_number:
  print("That's a draw!")
else:
  print("player wins!")



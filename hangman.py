import random
import hangman_data

#step 1 

word_list = ['alphabet', 'programing', 'football']


#TODO 1 - Randomly choose a word from the word_list and assign it to a var called chosen_word. Create a display var that contains as many _ as the number of letters in the word.

chosen_word = random.choice(word_list)
print(chosen_word) #remove to actually play

display = []

for letter in chosen_word:
    display += "_"

#TODO - Ask the user to guess a letter and assign their answer to a var called guess. Make guess lower_case

guess = ''
lifes = 6
end_game = False
print(hangman_data.logo)
print(hangman_data.HANGMANPICS[lifes] + f'\nYou start with {lifes} lifes.')

while not end_game:
  #Logic to make sure player only inputs one character.
  while True :
    guess = input("Guess a letter: \n").lower()
    if len(guess) == 1:
      print(f'Your character input was: {guess}')
      break
    print("Please enter a single character to continue.\n")

  #Manage player lifes
  if guess not in chosen_word:
    lifes -= 1
    print(f"The hidden word does not contain the letter chosen.\nYou have {lifes} lifes left.")
  #print hangman depending on how many lifes player has
  print(hangman_data.HANGMANPICS[lifes])

#Loop through each position in the chosen_word, if the given letter matches with any letter in the word, swap the blank space for the letter in the right position.
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print("Good choice!")
  print(display)

  #end the game, by either losing all lifes, or completing the word
  if lifes < 1:
    end_game = True
    print('You lost!')
  elif "_" not in display:
    end_game = True
    print("Congratulations, you have won!")

    

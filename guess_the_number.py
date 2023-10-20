from art import guess_the_number_logo
import random

random_number = random.randint(1, 100)

print(guess_the_number_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
  lifes = 10
elif difficulty == "hard":
  lifes = 5
else:
  print("Wrong input. Please type 'easy' or 'hard'.")

while lifes > 0:
  user_guess = int(input("Guess a number: "))
  if user_guess > random_number:
    lifes -= 1
    print("Ups too high. Gess lower.")
    print(f"You have {lifes} tries left")
  elif user_guess < random_number:
    lifes -= 1
    print("Ups too low! Guess higher.")
    print(f"You have {lifes} tries left")
  elif user_guess == random_number:
    print(f"Congratulations!! You guessed the number: {random_number}")
    lifes = 0
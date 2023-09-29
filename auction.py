from auction_data import logo
from os import system

print(logo)

bidders = {}
#clear = os.system('cls')

more_bidders = True
while more_bidders:
  name = input('What is your name?\n')
  bid = int(input('How much do you want to bid?\n$'))

  bidders.update({name : bid}) 

  keep_going = input("Would you like to continue? Yes or No\n").lower()
  if keep_going == "yes":
    more_bidders
    system("clear")
  else:
    more_bidders = False

highest_bidder = max(bidders)

print(bidders) # Remove if used in prod
print(highest_bidder)
print(bidders[highest_bidder]) # Remove if used in prod



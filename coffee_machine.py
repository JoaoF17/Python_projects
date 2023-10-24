from coffee_machine_data import MENU, resources

# print report
# are the resources enough 
# process coins
# check transaction sucessful
# Make coffe, deduct resources and give change back if any

profit = 0
resources = {
  'water' : 300,
  'milk' : 200,
  'coffee' : 100,
}

def is_resource_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
  return True
      

def process_coins():
  """Returns the total calculated from coins inserted

  Returns:
      int: Total value of inserted coins
  """  
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def is_transaction_successful(money_received, drink_cost):
  """Return True when the payment is sufficient, return False when the money is insuficcient

  Args:
      money_received (int): Money input by the user
      drink_cost (int): Cost of the drink purchased
  """  
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here's your change: ${change}")
    global profit
    profit += drink_cost
    return True
  else:
    print("Money not sufficient. Money refunded.")
    return False

def make_coffee(drink_name, coffee):
  for ingredient in coffee:
    resources[ingredient] -= coffee[ingredient]
  print(f"Here's your {drink_name}.")
  

machine_on = True
while machine_on:
  choice = input("What would you like? (Espresso || Latte || Cappuccino)\n").lower()
  if choice == "off":
    machine_on = False
  elif choice == "report":
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${profit}")
  else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
      payment = process_coins()
      is_transaction_successful(payment, drink["cost"])
      make_coffee(choice, drink['ingredients'])

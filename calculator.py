def add(a, b):
  """add operation
  """  
  return a + b

def minus(a, b):
  """minus operation
  """  
  return a - b

def multiply(a, b):
  """multiplication operation
  """  
  return a * b
  
def divide(a, b):
  """division operation
  """  
  return a / b

operations = {
  "+" : add,
  "-" : minus,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("Choose your first number:\n"))

for symbol in operations:
  print(symbol)
operation_symbol = input("Which symbol operation from above would you like to perform?\n")

num2 = int(input("Choose your second number:\n"))

calculation = operations[operation_symbol]
answer = calculation(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

again = True
while again:
  x = input("Would you like to do another calculation with the previous result? 'Yes' or 'No'\n").lower()
  if x == "no":
    again = False
  else:
    for symbol in operations:
      print(symbol)
    new_operation_symbol = input("Which symbol operation from above would you like to perform?\n")
    new_number = int(input("Choose a new number:\n"))
    new_calculation = operations[new_operation_symbol]
    new_answer = new_calculation(answer,new_number)
    print(f"{answer} {new_operation_symbol} {new_number} = {new_answer}")
    answer = new_answer
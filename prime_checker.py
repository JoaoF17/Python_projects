n = int(input("Which number do you want to check if it's a prime number: "))

def prime_check(number = n):
  is_prime = True
  
  for i in range(2, number-1):
    if number % i == 0:
      is_prime = False
  
  if is_prime == True:
    print(f"{n} is a prime number.")
  else:
    print(f"{n} is NOT a prime number.")

prime_check()



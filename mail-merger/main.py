with open("input/names.txt", "r") as names:
  names = names.read()
  # print(names)
  
name_list = names.split("\n")
print(name_list)

with open("input/email.txt") as email:
  email = email.read()
  
for name in name_list:
  new_email = email.replace("___", name)
  with open(f"output/{name}.txt", "w") as output:
    output.write(f"{new_email}")
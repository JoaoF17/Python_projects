import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(nato_csv)

dict1 = {}
#loop through def rows
for (index, row) in df.iterrows():
  dict1[row.letter] = row.code
  
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input()
letters = [letter.upper() for letter in user_input]

phonetic_list = []
for (key, value) in dict1.items():
  for letter in letters:
    if key == letter:
      phonetic_list.append(value)
      
print(phonetic_list)
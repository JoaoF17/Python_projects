import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("The word must start with a letter from the alphabet.")
    generate_phonetic()
  else:
    print(output_list)
    
generate_phonetic()
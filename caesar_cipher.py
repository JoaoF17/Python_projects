alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']

def caeser(dir, text_input, n_shift):
  end_text = ""

  for character in text_input:
    if character not in alphabet:
      end_text += character
    else:
      if dir == 'decode':
        position = int(alphabet.index(character))
        new_position = (position - n_shift)% 26
        end_text += alphabet[new_position]
      elif dir == 'encode':
        position = int(alphabet.index(character))
        new_position = (position + n_shift)% 26
        end_text += alphabet[new_position]
      else:
        print("The direction you entered is invalid")
    
  print(f"Your {dir}d message is {end_text}\n")
    

repeat = True
while repeat:

  direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
  text = input('Type your message:\n').lower()
  shift = int(input('Type the shift number:\n'))

  caeser (dir = direction, text_input = text, n_shift = shift)

  keep_going = input("Do you want to continue?\n").lower()
  if keep_going != "yes":
    repeat = False  


#First code iteration
# def encrypt(encrypt_text = text, n_shift = shift):
#   e_text = ''
#   for letter in encrypt_text:
#     index = int(alphabet.index(letter))
#     new_index = index + n_shift
#     if new_index > len(alphabet)-1:
#       new_index -= len(alphabet)
#     e_text += alphabet[new_index]
#   print(f"The encoded text is: {e_text}")

# def decrypt(decrypt_text = text, n_shift = shift):
#   d_text = ''
#   for letter in decrypt_text:
#     index = int(alphabet.index(letter))
#     new_index = index - n_shift
#     d_text += alphabet[new_index]
#   print(f"The decoded text is: {d_text}")

# if direction == "encode":
#   encrypt()
# elif direction == "decode":
#   decrypt()
# else:
#   print("The direction you entered is invalid")

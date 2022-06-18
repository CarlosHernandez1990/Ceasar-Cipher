import alphabet_bank

letter_bank = alphabet_bank.alphabet

choice = input('If you would like to encode a message type "encode". If you would like to decrypt a message type "decrypt".\n').lower()
message = input(f"Type in your message that you would like to {choice}:\n")
shift = int(input(f"Type in a number for the {choice}ing of your message\n"))

def encode(message, shift):
  encrypted = ""
  for letter in message:
    current_position = letter_bank.index(letter)
    new_position = current_position + shift
    if new_position >= len(letter_bank):
      new_position = len(letter_bank) - new_position
    encrypted += letter_bank[new_position]
    return encrypted



if choice == "encode":
  encode(message, shift)
elif 
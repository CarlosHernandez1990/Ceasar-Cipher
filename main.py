import alphabet_bank

letter_bank = alphabet_bank.alphabet

choice = input('If you would like to encode a message type "encode". If you would like to decrypt a message type "decrypt".\n').lower()

message = input(f"Type in your message that you would like to {choice}:\n")

shift = int(input("Type in a number for the {choice}ing of your message"))

def encode()

if choice == "encode":
  
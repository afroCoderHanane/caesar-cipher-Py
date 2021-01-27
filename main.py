from art import logo
print (logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar_cypher(text, shift, dir_):
  cypher_text=""
  for char in text:
    if char in alphabet:
      position= alphabet.index(char)
      if(dir_ == "encode"):
        new_position = position+shift
        if new_position>25:
          new_position = new_position%26
        cypher_text += alphabet[new_position]
      else:
        new_position = position - shift
        if(new_position<0):
          new_position+=26
        cypher_text+=alphabet[new_position]
    else:
      cypher_text+=char

  print(f"The encoded text is {cypher_text}")
#logo

#
choice = "no"
while(choice !="no"):
  caesar_cypher(text, shift, dir_=direction)
  choice = input("Type 'yes' to enter again or 'no' to end the program\n").lower()


# def decrypt(cyphered_text, shift):
#     decyphered_text=""
#     for i in range (len(cyphered_text)):
#        position = alphabet.index(cyphered_text[i])
#        new_position = position - shift
#        if(new_position<0):
#          new_position+=26
#        decyphered_text+=alphabet[new_position]
#     print(f"The encoded text is {decyphered_text}")
# if direction =="encode":
#   encrypt(text, shift)
# else:
#   decrypt(text, shift)
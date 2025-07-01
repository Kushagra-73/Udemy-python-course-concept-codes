alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo) 

def caesar(orignal_text,shift_amount,encode_or_decode):
    txt=""
    if encode_or_decode=="decode":            #out of code you have debugged this line of code
                shift_amount*=-1

    for letter in text:
        if letter not in alphabet:
            txt+=letter

        else:
            pos=alphabet.index(letter)+shift_amount
            pos%=len(alphabet)                 #0-25 index only 
            txt+=alphabet[pos]

    print(txt)

should_continue=True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(orignal_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()

    if restart=="yes":
        should_continue=True

    elif restart=="no":
        should_continue=False

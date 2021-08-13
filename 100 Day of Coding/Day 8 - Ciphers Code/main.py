#Ceaser Cipher 
import string

abc = [x for x in string.ascii_lowercase]*2



## create encrypt function with input direction and text 
## it will take texxt and ecnrypt it by offsetting the values 
def cryption(direction,plain_text,shift):
    cipher_text = ""
    for ltr in plain_text:
        idx = abc.index(ltr)
        if ltr not in abc:
            cipher_text += ltr
        elif direction == "encode":
            position = idx + (shift %26)
        elif direction == "decode":
            position = idx - (shift % 26)
        new_ltr = abc[position]
        cipher_text += new_ltr
    print(f"Your secret word is: {cipher_text}")


print(abc)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    cryption(direction,text,shift)

    cont = input("Do you want to continue? Yes or No?").lower
    if cont == "No":
        should_contine = False
    


print('''
                           88                   
            ""             88                                 
                           88                                 
 ,adPPYba,  88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     ""  88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b          88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa  88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
''')

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def lets_do(start_text,shift_amount,direction):
  end_text =""
  if direction  == "decode":
    shift_amount *= -1
  for char in start_text:
    if  char in alphabet:
      position = alphabet.index(char)
      new_position = position+shift_amount
      end_text+=alphabet[new_position]
    else:
      end_text += char # adds the char which are not there in teh list given above 
  print(f"The {direction}d message is {end_text}")



can_continue = True
while can_continue:
  dir= input ("Type encode to encrypt , Type decode to decrypt:\n")
  text = input("Enter your text here:\n")
  shift = int(input("Enter the shift numebr :\n"))
  # doene to overcome the index out of range error 
  shift = shift %26
   # calling the function to perform encoding or decoding
  lets_do(start_text=text,shift_amount=shift,direction=dir)

  response = input("Enter 'yes' if you want to do again or type 'no'.\n")
  if response == "no":
   can_continue = False
  print("********************************Ended************************************************")














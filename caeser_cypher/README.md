This code provides a Caesar cipher tool. It allows users to encrypt or decrypt messages by shifting letters in the alphabet based on a chosen number

for example 
![image](https://github.com/ThannojPallabothula/Projects/assets/160522282/83b504cb-1ca5-4e53-961b-87d3cb65aff5)



Encoding a message 

<img width="758" alt="image" src="https://github.com/ThannojPallabothula/Projects/assets/160522282/c0a3aaff-f963-4733-9fde-e41d3add3e73">


____________________________________________________________________________________________________________________________________________________________________________________________________


Decoding a message 
<img width="914" alt="image" src="https://github.com/ThannojPallabothula/Projects/assets/160522282/7dde0ad9-964d-4f42-b9cf-55cd96934dc8">



************************************ EXPLAINATION OF THE CODE ***********************************


what is happening in the code?

1:
=======

Declaring the Alphabet List:
A list named alphabet is created containing all lowercase letters twice. This list is used for character lookup during encryption and decryption.

2:
======
lets_do Function:    This function takes three arguments 
-----> start_text: The text entered by the user 
-----> shift_amount: An integer representing the number of positions to shift letters in the alphabet.
-----> direction: A string indicating whether to "encode" (encrypt) or "decode" (decrypt) the message.

The function (lets_do) iterates through each character in start_text.
If the character is a lowercase letter:
It finds the character's position in the alphabet list.
It adds (for encoding) or subtracts (for decoding) the shift_amount to this position.
It wraps around the alphabet using the modulo operator (%) to prevent going out of bounds.
It retrieves the new character from the alphabet list at the adjusted position and adds it to the end_text.
If the character is not a lowercase letter (e.g., space, punctuation), it's directly added to the end_text without modification.
Finally, the function prints the encoded/decoded message based on the provided direction.

3:
=======
Main Loop:

 can_continue is set to True to keep the program running.
While can_continue is True, the program loops:
It prompts the user to enter "encode" or "decode" based on their desired action.
It then requests a shift number, which gets adjusted using modulo (% 26) to ensure it stays within the alphabet range (0-25).
It calls the lets_do function with the user-provided information.
After processing, it asks the user if they want to continue. If "no", the loop ends, and a final message is printed.
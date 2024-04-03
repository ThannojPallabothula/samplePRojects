This code provides a Caesar cipher tool. It allows users to encrypt or decrypt messages by shifting letters in the alphabet based on a chosen number

for example 
<img width="626" alt="image" src="https://github.com/ThannojPallabothula/samplePRojects/assets/160522282/d86f7301-b976-4344-97f2-f19cbd449c37">



Encoding a message 
<img width="915" alt="image" src="https://github.com/ThannojPallabothula/samplePRojects/assets/160522282/4d64a3a6-32ab-4486-9fcd-60a047fea082">





____________________________________________________________________________________________________________________________________________________________________________________________________


Decoding a message
<img width="974" alt="image" src="https://github.com/ThannojPallabothula/samplePRojects/assets/160522282/1ba2bc7c-2e91-4df1-b2b5-b2b01e1ad8a1">





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

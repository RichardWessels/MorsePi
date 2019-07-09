# MorsePi

This program converts messages (with supported characters) to Morse Code. This Morse Code is then displayed on an LED connected to GPIO 15. 

Supported Characters:
a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 . , ?

All uppercase letters are converted to lowercase. 

The base unit determines the length of a dot. The standard is to have a dot equal to 1 second. If you want to follow this standard, set the base unit to 1. 

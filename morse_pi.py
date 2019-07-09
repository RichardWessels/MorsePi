import RPi.GPIO as gpio 
import time

morse_dict_raw = {
'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '.....', 'i': '..', 
'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
'9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..'
}

def rasp_setup():
    '''
    Sets up Raspberry Pi
    '''
    gpio.setmode(gpio.BCM)
    gpio.setup(15, gpio.OUT)
    gpio.output(15, False)

def morse_dict_spaces():
    '''
    Return (Dict): Morse Code dictionary with element spaces added
    '''
    new_dict = {}
    for key in morse_dict_raw:
        new_dict[key] = '0'.join(morse_dict_raw[key])
    return new_dict

def translate_word(word, morse_dict):
    '''
    Input (String): Word
    Return (String): Word converted into binary morse representation
    '''
    converted_word = []
    for char in word:
        print(char)
        converted_word.append(morse_dict[char])
    converted_word = '000'.join(converted_word)
    print(converted_word)
    return converted_word

def run_code(e, base_unit):
    '''
    Input (String): Morse element
    Output: LED activation
    Return: None
    '''
    if e in ['.','-']:
        gpio.output(15, True)
        if e == '.':
            time.sleep(base_unit)
        elif e == '-':
            time.sleep(base_unit*3)
        gpio.output(15, False)

    else:
        time.sleep(base_unit)

def main():
    rasp_setup()
    base_unit = 0.5
    morse_dict = morse_dict_spaces()

    continue_main = 'y'

    while continue_main == 'y':
        message = input("Enter message: ").lower().split(" ")
        words_defined = []

        for word in message:
            print("Word:", word)
            words_defined.append(translate_word(word, morse_dict))

        final_str = '0000000'.join(words_defined)

        for elem in final_str:
            print('Showing:', elem)
            run_code(elem, base_unit)

        print(final_str)

        continue_main = input("Press y to continue: ")[0].lower()
        
    gpio.cleanup()


if __name__ == "__main__":
    main()


# Features to add: Word and letter print

import RPi.GPIO as gpio 
import time

morse_dict_raw = {
'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '.....', 'i': '..', 
'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
'9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..'
}

def rasp_setup(gpio_pin):
    '''
    Sets up Raspberry Pi
    '''
    gpio.setmode(gpio.BCM)
    gpio.setup(gpio_pin, gpio.OUT)
    gpio.output(gpio_pin, False)

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
    Return (String): Word converted into Morse representation
    '''
    converted_word = []
    for char in word:
        try:
            print(char)
            converted_word.append(morse_dict[char])
        except IndexError:
            print(char, "is not in Morse dictionary. Character is skipped.")
    converted_word = '000'.join(converted_word)
    print(converted_word)
    return converted_word

def run_code(morse, base_unit, gpio_pin):
    '''
    Input (String): Morse element
    Output: LED activation
    Return: None
    '''
    for e in morse:
        if e in ['.','-']:
            gpio.output(gpio_pin, True)
            if e == '.':
                time.sleep(base_unit)
            elif e == '-':
                time.sleep(base_unit*3)
            gpio.output(gpio_pin, False)
        else:
            time.sleep(base_unit)

def main():
    gpio_pin = 15
    rasp_setup(gpio_pin)
    base_unit = 1
    morse_dict = morse_dict_spaces() # Add spacing

    continue_main = 'y'

    while continue_main == 'y':

        message = input("Enter message: ").lower()

        # List of words
        words_defined = message.split(" ")

        final_str = ""

        # Used to keep track of position in word to avoid extra spacing
        word_count = 0

        for word in words_defined:
            print(f"Current word {word}")
            word_count += 1

            # Same function as word_count, just for letters...
            letter_count = 0

            for char in word:
                print(f"Showing {char} as {morse_dict[char]}")
                letter_count += 1
                run_code(morse_dict[char], base_unit, gpio_pin)
                final_str += morse_dict[char]

                if letter_count != len(word):
                    run_code('000', base_unit, gpio_pin)
                    final_str += '000'
                    
            if word_count != len(words_defined):
                print("Running word space...")
                run_code('0000000', base_unit, gpio_pin)
                final_str += '0000000'

        print(final_str)

        continue_main = input("Press y to continue: ")[0].lower()
        
    gpio.cleanup()

if __name__ == "__main__":
    main()
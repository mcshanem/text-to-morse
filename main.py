from morse_mapping import morse_code_dict

# Print header
print('****************************')
print('Text to Morse Code Converter')
print('****************************')
print()

# Program loop
while True:
    print('Enter text to be converted to Morse code. Enter "qq" to quit.')
    # Store user input in 'text_input'
    text_input = input('Input: ')
    # Quit condition
    if text_input == 'qq':
        print('Quitting program')
        break
    # Convert text to morse code and print to output
    else:
        morse_output = []
        try:
            for letter in text_input.upper():
                morse_output.append(morse_code_dict[letter])
            print(f'Output: {" ".join(morse_output)}\n')
        except KeyError:
            print('Invalid input. Make sure you only use letters, numbers and punctuation.\n')

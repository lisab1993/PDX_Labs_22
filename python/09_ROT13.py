import string

# create a list with the lowercase alphabet
alphabet = []
for char in string.ascii_lowercase:
    alphabet.append(char)

# create a list of all punctuation and whitespace
extra_chars = []
punct = string.punctuation + ' '
for char in punct:
    extra_chars.append(char)

# list.index(element) gives us the index of the first occurrence of an element
# loop over the elements of the input string
# for every letter, find it's index in the alphabet list using .index()
# find the value of the index + 13
# if the value is over 25, take the value - 25, and the result will be the index of the encrypted letter
# if the value is 25 or under, then the index is naturally correct
input_string = input(
    'Enter a word or phrase that does not contain numbers to encrypt: ').lower()
encryption_level = int(
    input('How much rotation would you like in your encryption: '))

def rotate(user_input, encrypt):
    output_string = ''
    for char in user_input:
        if char.isnumeric():
            return 'Cannot encrypt - numbers are not allowed'
        else:
            if char in punct:
                output_string += char
            else:
                initial_index = alphabet.index(char)
                added = initial_index + encrypt
                if added <= 25:
                    output_string += alphabet[added]
                else:
                    difference = (added - 25) -1
                    output_string += alphabet[difference]
    return output_string

print(rotate(input_string, encryption_level))
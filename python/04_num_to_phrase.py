# Version 1
ones = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

user_input = int(input('Enter a number between 0 and 99: '))

# get the hundreds, tens, and ones positions
if len(str(user_input)) < 3:
    ones_digit = user_input % 10
    tens_digit = user_input//10

# display the English representation
if user_input < 10:
    print(ones[user_input])
elif user_input < 20:
    print(teens[ones_digit])
elif user_input < 100:
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        print(f'{tens[tens_digit]}-{ones[ones_digit]}')
##################################################################
# Version 2
# Version 2 uses the dictionaries and user input from version 1, and is a continuation of an if statement from version 1.
elif user_input < 1000:
    ones_digit = user_input % 10
    hundreds_digit = user_input//100
    tens_digit = (user_input-(hundreds_digit*100))//10
    if tens_digit == 0 and ones_digit == 0:
        print(f'{ones[hundreds_digit]} hundred')
    elif tens_digit == 0 and ones_digit != 0:
        print(f'{ones[hundreds_digit]} hundred and {ones[ones_digit]}')
    elif tens_digit == 1:
        print(f'{ones[hundreds_digit]} hundred and {teens[ones_digit]}')
    elif tens_digit != 0 and ones_digit == 0:
        print(f'{ones[hundreds_digit]} hundred and {tens[tens_digit]}')
    else:
        print(
            f'{ones[hundreds_digit]} hundred and {tens[tens_digit]}-{ones[ones_digit]}')

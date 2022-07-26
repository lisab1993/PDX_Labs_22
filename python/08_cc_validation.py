

def cc_valid(cc_string):
    # conver to a list of ints
    cc_list = []
    for char in cc_string:
        cc_list.append(int(char))

    # remove last digit and create the check digit
    check = cc_list.pop()

    # reverse the list
    cc_list.reverse()

    # double every other element starting with the first number
    for i in range(len(cc_list)):
        # check if the index is even to double the correct elements
        if i % 2 == 0:
            is_even = True
        else:
            is_even = False
        # double the even elements and add them to the list
        if is_even == True:
            doubled = cc_list[i] * 2
            cc_list[i] = doubled

    #subtract nine from all number over nine
    for i, num in enumerate(cc_list):
        if num > 9:
            cc_list[i] = num-9

    # sum all the values
    sum = 0
    for num in cc_list:
        sum += num

    # take the second digit of that sum
    second_digit = int(str(sum)[1])
    if check == second_digit:
        return True
    else:
        return False


card = input('Enter a credit card number all together, without spaces: ')
valid = cc_valid(card)

if valid == True:
    print('Your card is valid')
else:
    print('Your card is invalid')

import math

# version 1

nums = [5, 0, 8, 3, 4, 1, 6]

# print((5.3).is_integer())
def average(list):
    #create a sum of the given array
    sum = 0
    for num in list:
        sum += num
    #find the average of the list
    list_len = len(list)
    output = sum/list_len
    #display whole numbers as integers, and decimal numbers rounded to the second digit. 
    #is_integer takes in a float, and checks if it's a whole number that can be displayed as an integer; it returns True or False
    if (output).is_integer():
        output = int(output)
    else:
        output = round(output, 2)
    return f'The answer is {output}'

# print(average(nums))

# version 2

nums_list = []
while True:
    new_num = input('Enter a number, or "done" to finish: ')
    if new_num == 'done' or new_num == 'Done':
        break
    else:
        nums_list.append(int(new_num))

print(average(nums_list))


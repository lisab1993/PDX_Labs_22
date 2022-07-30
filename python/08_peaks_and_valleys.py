
import enum
# Version 1

def peaks(array):
    '''Return indicies of peaks - lower number on left and right'''
    peaks_output = []
    for i, num in enumerate(array):
        # first and last numbers don't have parters on both sides, so skip them
        if i != 0 and i != len(array)-1:
            if array[i-1] < num and array[i+1] < num:
                peaks_output.append(i)
    return peaks_output


def valleys(array):
    '''Return indices of valleys - higher number on left and right'''
    valleys_output = []
    for i, num in enumerate(array):
        # first and last numbers don't have parters on both sides, so skip them
        if i != 0 and i != len(array)-1:
            if array[i-1] > num and array[i+1] > num:
                valleys_output.append(i)
    return valleys_output


def peaks_and_valleys(array):
    '''Returns indices of peaks and valleys in order of appearance'''
    # the first peak or valley found will naturally have the lowest index, so we just need to combine the lists and sort from lowest to highest.
    peak_arr = peaks(array)
    valley_arr = valleys(array)
    combined_arr = peak_arr + valley_arr

    return combined_arr


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Answer to version one below this line
# print(peaks_and_valleys(data), 'peaks and valleys')

# ------------------------------------------------------
# Version 2

# make a blank output string, and keep adding whitespaces and Xs
# find the value of the highest peak in the list, and store it in a variable called highest_value - we will not change this variable because our first for loop depends on it (must be declared outside the loops)
# create another variable called current_value, and make it equal to the highest peak as well - we will update this variable in a loop later on to get the correct X or whitespace while iterating (must be declared outside the loops).
# first for loop: use a for loop over the range of highest_value to get the correct height of the peaks
# nested for loop: inside that for loop, nest another for loop that iterates over the elements of the data list
# within the nested for loop: for every element, add either an X or a whitespace, depending on if the element is greater than or equal to current_value
# everytime the nested loop finishes an iteration, reduce current_value by 1, and add a new line escape character to the output string


# Answer to version 2 below this line (uncomment the whole code block)
# output = ''
# highest_value = int(peaks_and_valleys(data)[-1])
# current_value = int(peaks_and_valleys(data)[-1])
# for i in range(highest_value):
#     for i, num in enumerate(data):
#         if num >= current_value:
#             output += f' X '
#         else:
#             output += f'   '
#     output += '\n'
#     current_value -= 1
# print(output)

#-----------------------------------------------------------

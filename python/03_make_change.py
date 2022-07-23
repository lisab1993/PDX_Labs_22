#version 1

# dollar = float(input('Enter a dollar amount: '))
# total = int(dollar * 100)

# quarters = total // 25
# total = total - quarters * 25

# dimes = total // 10
# total = total - dimes * 10

# nickels = total // 5
# total = total - nickels * 5

# print(f'{dollar} breaks into {quarters} quarters, {dimes} dimes, {nickels} nickels, and {total} pennies.')

###############################################################

#version 2

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

dollar = float(input('Enter a dollar amount: '))
total = int(dollar * 100)

#we'll add on to this string, and return it at the end
output = 'there '
for coin in coins:
    
    #determine the number of coins for each coin in the list
    coin_amount = total // coin[1]
    total = total - coin_amount * coin[1]

    # if there's only 1 half-dollar, we want to say 'there is' in our output; otherwise, we want to say 'there are' in our output
    if 

    #grab the last letter of the coin name for grammatical reasons
    last_letter = coin[0][len(coin[0])-1]

    #if the coin amount is not exactly 1, then we want to refer to the plural version of the coin name. 
    if coin_amount != 1:
        #if the coin name ends in 'y', we have to replace 'y' with 'ies'; otherwise, we can just add an s at the end
        if last_letter != 'y':
            output += f'{coin_amount} {coin[0]}s '
        else:
            grammar = coin[0].replace(last_letter, 'ies ')
            output += f'{coin_amount} {grammar}'
    #if the coin amount is 1, then we want to refer to the singular version of the coin name
    else:
        output += f'{coin_amount} {coin[0]} '
    
    #add an 'and' before the last coin 
    if coin_index == len(coins)-2:
        output += 'and '

print(output)

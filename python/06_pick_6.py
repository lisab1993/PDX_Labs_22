import random

# Version 1
def pick6():
    '''Creates a new ticket; can be the winning ticket, or a guessing ticket'''
    new_ticket = []
    for i in range(6):
        new_ticket.append(random.randint(1, 99))
    return new_ticket

# the winning ticket all other tickets will be compared to
winning_ticket = pick6()
cost_of_ticket = 2
tickets_to_buy = 100000

#how much money has been spend and earned, starting from 0
balance = 0

#add money to the balance, depending on how many matches a ticket has
matches_to_cash = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

#earnings is how much money we won from ticket matches
earnings = 0
for i in range(tickets_to_buy):
    #generate a ticket, subtract the cost of the ticket, and check for matches
    guessing_ticket = pick6()
    balance -= cost_of_ticket
    ticket_matches = 0
    for i in range(len(winning_ticket)):
        if guessing_ticket[i] == winning_ticket[i]:
            ticket_matches += 1
    #add the earnings from the matches to the balance
    earnings += matches_to_cash[ticket_matches]

balance += earnings
# print(f'After buying the tickets and calculating the matches, your final balance is ${balance}')

# Version 2
#expenses is the cost of a ticket multiplied by the number of tickets bought
expenses = tickets_to_buy * cost_of_ticket
roi = (earnings - expenses)/expenses

print(f'Final balance: ${balance} \nEarnings: ${earnings} \nExpenses: ${expenses} \nROI: {roi}')
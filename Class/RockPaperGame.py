"""
mkp
"""

from random import random

def get_input():
    '''Asks the user for the number of rounds in the tournament
    and the number of times to simulate the tournament
    input: none
    output: r and simnum'''

    r = int(input("Enter the number of rounds in the tournament: "))
    simnum = int(input("Enter the number of tournaments to simulate: "))
    return r, simnum
    

def simmatch():
    '''Simulate a single best of 3 match of rock paper scissors
    input: none
    output: True if you won, False if you lost'''
    wins = 0
    losses = 0
    while (wins < 2 and  losses < 2):  # ERROR was here; we keep going until we have less winns and losses
        throw = random() # generates random number between 0 and 1
        if throw < 0.5:
            wins += 1
        elif throw < 0.7:
            losses += 1
        else:
            pass
        
    if wins == 2:
        return True
    else:
        return False
        


def simtourn(r):
    '''Simulates a single r-round tournament
    input: r (the number of rounds)
    output: True if you won the tournament, False if you lost'''
    for i in range(r):
        won = simmatch()
        if won is False: # losing single game
            return False
    return True
        
    


def simulate(simnum, r):
    '''Given input simnum and r, simulates simnum number of
    r-round tournaments.
    input: simnum and r
    output: wins and losses'''
    wins = 0
    losses = 0
    for i in range(simnum):
        result = simtourn(r)
        if result:
            wins += 1
        else:
            losses += 1
    return wins, losses

    
      

def report(wins, losses, simnum):
    '''Given input wins and losses, prints the number of tournaments
    the user won, the number the user lost, and their win percentage
    input: wins and losses
    output: none, but prints out the data as above'''
    winpercentage = 100*(wins/(wins+ losses))
    print("You won", wins, "tournaments.")
    print("You lost", losses, "tournaments.")
    print("Your win percentage was", winpercentage)


def main():
    r, simnum = get_input()
    wins, losses = simulate(simnum, r)
    report(wins, losses, simnum)

main()

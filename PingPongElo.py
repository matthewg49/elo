#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:11:46 2017

@author: matthewgonzalez
"""
import math as m

#elo rating function
def pingpong_rating(elow, elol, mov=2, k=15):
    #with margin of victory(MOV), k factor and elo of winner/elo of loser
    k_mult_with_mov = (m.log(abs(mov)+1)) * (2.2/((elow-elol)*.001+2.2))
    rp1 = 10**(elow/400)
    rp2 = 10**(elol/400)
    prob_elow = rp1/float(rp1+rp2)
    prob_elol = rp2/float(rp1+rp2)
    new_elow = elow + k_mult_with_mov*k*(1-prob_elow)
    new_elol = elol + k_mult_with_mov*k*(0-prob_elol)
    return int(new_elow), int(new_elol)


#Sample of "All players"
all_players = {'Matthew Gonzalez': 1500, 'Eric Dickinger': 1500, 'Jake Mehring': 1500}

#Conditional statements that allow the user to interact with the program. DB support coming soon
while True:
    choice = int(input(
    """Welcome to the IAPPLLA Elo system! Please make a choice below:\n1. View a player's ELO\n2. View all player ratings\n3. Record a match\n"""))
    
    #Choice 1
    if choice == 1:
        which = input("Who's ELO would you like to see? (Full Name): ")
        print("Here is the elo of " + which + ": " + str(all_players[which]))
    
    #Choice 2
    if choice == 2:
        for k,v in all_players.items():
            print(k.title() + ": " + str(v) + "\n")
    
    #Choice 3
    if choice == 3:
        win = input('Who was the winner? ')
        lose = input('Who was the loser ')
        margin = int(input('Waht was the margin of vicotry?: '))
        if win not in all_players:
            all_players[win] = 1500
        if lose not in all_players:
            all_players[lose] = 1500
        new_scoresw, new_scoresl = pingpong_rating(all_players[win], all_players[lose], mov=margin)
        all_players[win] = new_scoresw
        all_players[lose] = new_scoresl
        print("The new elo for the winner, " + win + " is: " + str(all_players[win]))
        print("The new elo for the loser, " + lose + " is: " + str(all_players[lose]))               
    
    repeat = input("Would you like to select another option from the list above? (yes/no)")
    if repeat == "no":
        break
                       
    
            
        



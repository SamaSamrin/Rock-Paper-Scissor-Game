# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:51:32 2022

@author: Sama Samrin
"""

import random
    
"""
function to determine who won.
Conditions: paper beats rock, rock beats scissors, scissor beats paper
"""
def has_won(player1_shot, player2_shot):
    if (player1_shot=='p' and player2_shot=='r') or (player1_shot=='r' and player2_shot=='s') or (player1_shot=='s' and player2_shot=='p'):
        return player1_shot
    else:
        return player2_shot

"""
function for taking inputs for the main moves and checking results
"""
def play():
    user_shot = input("Enter 'p' for paper, 's' for scissor, or 'r' for rock\n").lower()
    computer_shot = random.choice(['r', 'p', 's']).lower()

    print("user:", user_shot)
    print("computer:", computer_shot)
      
    if user_shot == computer_shot:
        print("It's a Tie!")
    else:
        result = has_won(user_shot, computer_shot)
        if result==user_shot:
            print("Congrats! You won!")
        else:
            print("Sorry, You Lost")

number = int(input("How many times do you want to play?\n"))
for i in range(number):
    play()
                
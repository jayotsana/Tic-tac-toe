# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:57:56 2019

@author: Neha
"""


# tic tac toe game

import os
import time 
#import random

# draw the board
board = ['', ' ', ' ', ' ' ,' ',' ',' ',' ',' ',' ']

# draw the board
def draw_board():
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))

# X win 
def X_win(board):
    if board[1] == 'X' and board[2] == 'X' and board[3] == 'X' or \
        board[4] == 'X' and board[5] == 'X' and board[6] == 'X' or \
        board[7] == 'X' and board[8] == 'X' and board[9] == 'X' or \
        board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or \
        board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or \
        board[3] == 'X' and board[6] == 'X' and board[9] == 'X' or \
        board[1] == 'X' and board[5] == 'X' and board[9] == 'X' or \
        board[3] == 'X' and board[5] == 'X' and board[7] == 'X':

        return True
    else:
        return False    
# O win
def O_win(board):
    if board[1] == 'O' and board[2] == 'O' and board[3] == 'O' or \
        board[4] == 'O' and board[5] == 'O' and board[6] == 'O' or \
        board[7] == 'O' and board[8] == 'O' and board[9] == 'O' or \
        board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or \
        board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or \
        board[3] == 'O' and board[6] == 'O' and board[9] == 'O' or \
        board[1] == 'O' and board[5] == 'O' and board[9] == 'O' or \
        board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
        return True
    else:
        return False    

while True:
    try:
        os.system('clear')
        draw_board()
        choice = int(input('Please choose the empty space for X :: '))
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print('Sorry, that space is no empty!')
            time.sleep(1)

        # if the X win
        if X_win(board):
            os.system('clear')
            draw_board()
            print('X is win !')
            break
        
        # space is full or not
        is_full = True
        for index in range(1,10):
            if board[index] == " ":
                is_full = False
                break

        # tie the game
        if is_full == True:
            os.system('clear')
            draw_board()
            print('Tie the game!')
            break    

        os.system('clear')
        draw_board()
        choice = int(input('Please choose the empty space for O : '))
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print('Sorry, that space is no empty!')
            time.sleep(1)
        
        # if the O win 
        if O_win(board):
            os.system('clear')
            draw_board()
            print('O is win !')
            break

        # check the board game
        is_full = True
        for index in range(1,10):
            if board[index] == " ":
                is_full = False
                break
    
        # tie game
        if is_full == True:
            os.system('clear')
            draw_board()
            print('Tie the game!')
            break
    except Exception as ex:
 
       print(ex)
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# created by Matthew Mullen, followed consultation model where we talked about algorithms to solve (using bools to sort out turns and using getter functions)
from UltimateMetaTTT import NumTicTacToe, MetaTicTacToe, ClassicTicTacToe


def gametype(board,row,col):
    if board[row][col].lower()=='n':
        string='Numerical Tic Tac Toe'
        return string
    if board[row][col].lower()=='c':
        string='Classical Tic Tac Toe'
        return string
    
# player1_turn asks for who's playing, true for player 1 who picks odd numbers and false for player 1 who picks even numbers
# previous_num is the is the numbers that has been entered and stored so the user can't repeat them
def num_input(player1_turn,previous_num):
    if player1_turn==True:
        player='1'
        number_choice='odd number (1-9).'
    else:
        player='2'
        number_choice='even number (2-8)'
    stat=False
    while stat==False:
        update=input('player %s, please enter an %s '% (player,number_choice))
        if player=='1':
            try:
                
                if int(update)%2==1:
                    if int(update) not in previous_num:
                        
                        stat=True
                    else:
                        print('Error: that number has already been entered.')
                else:
                    print('Error: entry not odd.')
            except:
                print('Invalid input')
            
        if player=='2':
            try:
                if int(update)%2==0:
                    if int(update)>0:
                        if int(update) not in previous_num:
                            stat=True
                        else:
                            print('Error: that number has already been entered')
                else:
                    print('Error: not an even number')
            except:
                print('Reenter your update. Error occurred.')
    update=int(update)
    return update
# gets the row number from user
def getrow(player):
    
    valid_getrow=False
    while valid_getrow==False:
            # did not convert to int in the next line so that it would not crash from error if input was letter
            row=input('player %s, please enter a row.  '% player)
            try:
                if int(row) in range(0,3):
                    valid_getrow=True
                else:
                    print('Error:please enter a row number in range 3' )
            except:
                print('Error: row not in correct range.')
                
    row=int(row)
    return row
# gets the column number from user
def getcol(player):
    valid_getcol=False
    while valid_getcol==False:
            col=input('player %s, please enter a col. '%player)
            try:
                if int(col) in range(0,3):
                    valid_getcol=True
                if int(col) not in range(0,3):
                    print('Error: column not in correct range.')
            except:
                print('Error: col not in correct range.')
    col=int(col)
    return col

def play_again():
    
    ver_input=False
    while ver_input==False:
        user_inp=input('Do you want to play another game? (Y/N)')
        if user_inp.lower()=='n':
            ver_input=True
            print('Thanks for playing! Goodbye.')
            return False
        if user_inp.lower()=='y':
            ver_input=True
            return True
        

    
def play_local_game(game,player1s_turn):
    
    game.drawBoard()
    preventered=[]
    while game.isWinner()==False and game.boardFull()==False:
        
        if game.isNum()==True:
            player=player_turn(player1s_turn)
            num=num_input(player1s_turn,preventered)
            preventered.append(num)
            
            row=getrow(player)
            col=getcol(player)
            if game.squareIsEmpty(row,col)==False:
                print('Error invalid move')
                while not game.squareIsEmpty(row,col):
                    num=num_input(player1s_turn,preventered)
                    row=getrow(player)
                    col=getcol(player)
            game.update(row,col,num)
            game.drawBoard()
            if game.update(row,col,num)==True:
                preventered.append(num)
            player1s_turn=changeturns(player1s_turn)
        if game.isNum()==False:
            player=player_turn(player1s_turn)
            row=getrow(player)
            col=getcol(player)
            if game.squareIsEmpty(row,col)==False:
                print('Error could not make a move')
                while game.squareIsEmpty(row,col)==False:
                    row=getrow(player)
                    col=getcol(player)
            if player=='1':
                mark='X'
            if player=='2':
                mark='O'
            
            game.update(row,col,mark)
            game.drawBoard()
            player1s_turn=changeturns(player1s_turn)
            
    if game.isWinner()==True:
        player1s_turn=changeturns(player1s_turn)
        return player_turn(player1s_turn)
    if game.boardFull()==True:
        player1s_turn=changeturns(player1s_turn)
        return ('draw',player_turn(player1s_turn))
    
def player_turn(player1_turn):
    
    if player1_turn==True:
        return '1'
    if player1_turn==False:
        return '2'
def changeturns(player1_turn):
    
    if player1_turn==True:
        return False
    if player1_turn==False:
        return True
def main():
    
    play=True
    while play==True:
        global_game=MetaTicTacToe('MetaTTTconfig.txt')
        print('----------------------------------')
        print('Starting new Meta Tic Tac Toe game')
        print('----------------------------------')
        player1_turn=True
        while not global_game.isWinner() and not global_game.boardFull():
            global_game.drawBoard()
            if player1_turn==True:
                player='1'
            else:
                player='2'
            row=getrow(player)
            col=getcol(player)
            print('----------------------------------')
            local_game=global_game.getLocalBoard(row,col)
            print('This is ', gametype(global_game.board,row,col))
            while not local_game.isWinner() and not local_game.boardFull():
                outcome=play_local_game(local_game,player1_turn)
                if outcome=='1'or outcome=='2':
                    print(outcome+' wins. Congrats!')
                if outcome[0]=='draw':
                    print('It is a tie.')
                player1_turn=changeturns(player1_turn)
            if outcome=='1':
                global_game.update(row,col,'X')
            if outcome=='2':
                global_game.update(row,col,'O')
            if outcome[0]=='draw':
                global_game.update(row,col,'D')
        global_game.drawBoard()
        print(outcome+' wins the Meta Tic Tac Toe game. GOOD GAME!')
        play_again()
        if play_again()==False:
            play=False
        if play_again()==True:
            play=True            
main()            


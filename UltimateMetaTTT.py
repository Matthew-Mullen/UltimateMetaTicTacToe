class NumTicTacToe:
    
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
        
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        for i in range(len(self.board)):
            
                for j in range((len(self.board))):
                    if self.board[i][j]==0:
                        self.board[i][j]=' '
       
        print('    0   1   2')
        for i in range(len(self.board)):
            
            print(' %d  %s | %s | %s' % (i,self.board[i][0],self.board[i][1],self.board[i][2]))
            print('   '+'-'*11)
        
        
                
        
        


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''

        if self.board[row][col]==' 'or self.board[row][col]==0:
            return True
        
        return False
        
        
    
    # mark is an int for users input in range(1-10)
    def update(self, row, col, mark):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        if mark not in range(1,10):
            raise Exception('Error:Number not in range 10.')
        if self.squareIsEmpty(row,col)==True:
            self.board[row][col]=mark
            
            return True
            
        if self.squareIsEmpty(row,col)==False:
            
            return False
        
       
        
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        nonempty_list=[]
        
        for i in self.board:
            
            for j in range(len(self.board)):
                if i[j]!=' ' and i[j]!=0:
                    nonempty_list.append(i[j])
        
        
        if len(nonempty_list)<self.size**2:
            return False
        return True
        
           
    def isWinner(self):
        '''
        Checks if any win conditions exist (3 in a row adding to 15)
        Inputs: none
        Returns: True if there is a win condition that exists on the board; False otherwise
        '''
        for i in self.board:
            
            for j in range(len(self.board)):
                if i[j]==' ':
                    i[j]=0
        
            
        #  we check if any diagonal, vertical, horizontal adds to 15 
        
        
        
        
        if (self.board[0][0]+self.board[1][0]+self.board[2][0]==15):
                
        
            return True 
                
        if (self.board[0][2]+self.board [1][2]+self.board[2][2]==15):
                
            
            return True
                
        if self.board[0][1]+self.board [1][1]+self.board[2][1]==15:
                
            
            return True
                
        if self.board[0][0]+self.board[0][1]+self.board[0][2]==15:
        
            
                    
            return True
        
        if self.board[1][0]+self.board [1][1]+self.board[1][2]==15:
            
            return True
                
        if self.board[2][0]+self.board [2][1]+self.board[2][2]==15:
            
            return True
            
            
        if (self.board[0][0]+self.board[2][2]+self.board[1][1]==15):
                    
            
            return True
                        
            
        if (self.board[0][2]+self.board[2][0]+self.board[1][1]==15):
                    
            
            return True
            
            
            
        return False
    def isNum(self):
        '''
        Inputs: none
        Returns: True 
        '''
        
        
        return True
        
        
        

class ClassicTicTacToe:
    
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] 
        self.size = 3   
        
        # populate the empty squares in board with empty string
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(' ')
            self.board.append(row)
        
        
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        
        l1='    0   1   2'
        print(l1)
        for i in range(len(self.board)):
            
            print(' %d  %s | %s | %s' % (i,self.board[i][0],self.board[i][1],self.board[i][2]))
            print('   '+'-'*11)
            
                                           
                                         


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''

        if self.board[row][col]==' ':
            return True
        
        return False
        
                
        
        
        
    
    # mark is a string for the users input of x or o
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (string) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        
        if self.squareIsEmpty(row,col)==True:
            self.board[row][col]=mark.upper()
            
            return True
            
        if self.squareIsEmpty(row,col)==False:
            
            return False
        
        
        
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        nonempty_list=[]
        
        for i in self.board:
            for j in range(len(self.board)):
                if i[j]!=' ':
                    nonempty_list.append(i[j])
        
        
        if len(nonempty_list)<self.size**2:
            return False
        return True
        
           
    def isWinner(self):
        '''
        Checks the board for any win conditions (3 of a kind in a row)
        Inputs: none
        Returns: True if a win condition exists on the board; False otherwise
        '''
        for i in range(len(self.board)):
            if self.board[i][0]+self.board[i][1]+self.board[i][2]==(3*'X') or self.board[i][0]+self.board[i][1]+self.board[i][2]==(3*'O'):
                return True
            if self.board[0][i]+self.board[1][i]+self.board[2][i]==(3*'X') or self.board[0][i]+self.board[1][i]+self.board[2][i]==(3*'O'):
                return True
            
        if self.board[0][0]+self.board[2][2]+self.board[1][1]==(3*'X') or self.board[0][0]+self.board[2][2]+self.board[1][1]==(3*'O'):
            return True
        if self.board[0][2]+self.board[2][0]+self.board[1][1]==(3*'X') or self.board[0][2]+self.board[2][0]+self.board[1][1]==(3*'O'):
            return True
            
        return False
    def isNum(self):
        '''
        Inputs: none
        Returns: False 
        '''
        
        return False
        
        
               




class MetaTicTacToe:
    def __init__(self,configFile):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        open_file=open('MetaTTTconfig.txt','r')
        file=open_file.read()
        # creates list containing lists by splitting on new lines and then on blank spaces 
        # this allows it to be any size of grid
        row=file.split('\n')
        for i in row:
            self.board.append(i.split(' '))
        open_file.close()
        
        
        
        
                
        
        
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        
        
        print('    0   1   2')
        for i in range(len(self.board)):
            
            print(' %d  %s | %s | %s' % (i,self.board[i][0],self.board[i][1],self.board[i][2]))
            print('   '+'-'*11)
            
                                           
                                         


    def squareIsEmpty(self, row, col):
        '''
        Checks if there is an unplayed local board at the given spot
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is unplayed; False otherwise
        '''

        if self.board[row][col].lower()=='n' or self.board[row][col].lower()=='c':
            return True
        
        return False
        
                
        
        
        
    
    
    def update(self, row, col, result):
        '''
        updates global board with winners of local board game instances
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (string) - update to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        
        if self.squareIsEmpty(row,col):
            
            self.board[row][col]=result.upper()
            
            return True
            
        
            
        return False
        
        
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining local boards to be played.
        Inputs: none
        Returns: True if the board has no unplayed local boards (full); False otherwise
        '''
        finished_list=[]
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j]!='n' and self.board[i][j]!='c':
                    finished_list.append(self.board[i][j])
        
        
        if len(finished_list)<self.size**2:
            return False
        return True
        
           
    def isWinner(self):
        '''
        Checks if any win conditions of the global game exist on global board
        Inputs: none
        Returns: True if any win conditions exist; False otherwise
        '''
        
        
       
        for i in range(len(self.board)):
            if self.board[i][0]+self.board[i][1]+self.board[i][2]==(3*'X') or self.board[i][0]+self.board[i][1]+self.board[i][2]==(3*'O')or self.board[i][0]+self.board[i][1]+self.board[i][2]==(3*'D'):
                return True
            if self.board[0][i]+self.board[1][i]+self.board[2][i]==(3*'X') or self.board[0][i]+self.board[1][i]+self.board[2][i]==(3*'O')or self.board[0][i]+self.board[1][i]+self.board[2][i]==(3*'D'):
                return True
        # diagonal win conditions
        if self.board[0][0]+self.board[2][2]+self.board[1][1]==(3*'X') or self.board[0][0]+self.board[2][2]+self.board[1][1]==(3*'O')or self.board[0][0]+self.board[2][2]+self.board[1][1]==(3*'D'):
            return True
        if self.board[0][2]+self.board[2][0]+self.board[1][1]==(3*'X') or self.board[0][2]+self.board[2][0]+self.board[1][1]==(3*'O')or self.board[0][2]+self.board[2][0]+self.board[1][1]==(3*'D'):
            return True
            
            
            
        return False
    def getLocalBoard(self,row,col):
        '''
        Checks if the board has any remaining local boards to be played.
        Inputs: row,col both ints
        Returns: instance of one of the two types of local boards
        '''
        
        if self.board[row][col]=='n':
            return NumTicTacToe()
        if self.board[row][col]!='n':
            return ClassicTicTacToe()
        

        
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    # vertical win condition test for classic true if win
    
    print('Classic tic tac toe vertical win condition, this tests update, drawBoard, and isWinner \n')
    new_game=ClassicTicTacToe()
    new_game.update(0,1,'x')
    new_game.update(1,1,'x')
    new_game.update(2,1,'x')
    new_game.drawBoard()
    print(new_game.isWinner())
    
    # horizontal win condition test for classic true if win
    print('\n')
    print('Classic tic tac toe horizontal win condition')
    new_game=ClassicTicTacToe()
    new_game.update(1,0,'x')
    new_game.update(1,1,'x')
    new_game.update(1,2,'x')
    new_game.drawBoard()
    print(new_game.isWinner())
    
    # diagonal win condition test for classic 
    
    print('Classic tic tac toe diagonal win condition ')
    new_game=ClassicTicTacToe()
    new_game.update(0,0,'x')
    new_game.update(1,1,'x')
    new_game.update(2,2,'x')
    new_game.update(1,0,'o')
    new_game.drawBoard()
    print(new_game.isWinner())
    
    # vertical win condition test for numerical 
    
    print('Numerical tic tac toe vertical win condition')
    new_game=NumTicTacToe()
    new_game.update(0,0,5)
    new_game.update(1,0,5)
    new_game.update(1,1,8)
    new_game.update(2,0,5)
    new_game.drawBoard()
    print(new_game.isWinner())
    
    # horizontal win condition test for numerical true if win
    print('\n')
    print('Numerical tic tac toe horizontal win condition')
    new_game=NumTicTacToe()
    new_game.update(0,0,5)
    new_game.update(0,1,5)
    new_game.update(0,2,5)
    new_game.drawBoard()
    print(new_game.isWinner())
    
    # diagonal check for not win condition test for numerical false if not win
    print('\n')
    print('Numerical tic tac toe diagonal ')
    new_game=NumTicTacToe()
    new_game.update(0,0,5)
    new_game.update(1,1,5)
    new_game.update(2,2,4)
    new_game.drawBoard()
    print(new_game.isWinner())
    
    #full board test for classic 
    
    print('boardFull test for classic ttt')
    new_game=ClassicTicTacToe()
    new_game.update(0,0,'x')
    new_game.update(1,0,'x')
    new_game.update(2,0,'x')
    new_game.update(0,1,'x')
    new_game.update(1,1,'x')
    new_game.update(2,1,'x')
    new_game.update(0,2,'x')
    new_game.update(1,2,'x')
    new_game.update(2,2,'x')
    new_game.drawBoard()
    print(new_game.boardFull())
    
    # is square empty test on classic 
    
    print('squareIsEmpty test for classic ttt')
    new_game=ClassicTicTacToe()
    new_game.update(0,0,'x')
    new_game.drawBoard()
    print(new_game.squareIsEmpty(0,0))
    # is square empty test on num returns true if empty
   
    print('squareIsEmpty test for numerical')
    
    new_game=NumTicTacToe()
    new_game.update(0,0,1)
    new_game.drawBoard()
    print(new_game.squareIsEmpty(0,1))
    
    # checks isNum
    
    print('isNum test for numeric')
    new_game=NumTicTacToe()
    print(new_game.isNum())
    
    print('isNum test for classic')
    new_game=ClassicTicTacToe()
    print(new_game.isNum())
    
    
    
    # now we test metatictactoe
    
    new_game=MetaTicTacToe('MetaTTTconfig.txt')
    print('drawBoard test for meta ttt ')
    new_game.drawBoard()
    
    print('isWinner test for meta')
    
    print(new_game.isWinner())
    
    # vertical win meta
    new_game.update(0,0,'X')
    new_game.update(0,1,'X')
    new_game.update(0,2,'X')
    new_game.drawBoard()
    print(new_game.isWinner())
    
    
  
    print('this provides us with the type of object of localboard ')
    
    print(new_game.getLocalBoard(0,0))
    
    print(new_game.getLocalBoard(1,1))
    
    # here we test boardFull by checking when empty and when full
    
   
    print(new_game.boardFull())
    
    
    print('check for a full board ')
    new_game.update(1,0,'X')
    new_game.update(1,1,'x')
    new_game.update(1,2,'X')
    new_game.update(2,0,'x')
    new_game.update(2,1,'X')
    new_game.update(2,2,'X')
    new_game.drawBoard()
    
    print(new_game.boardFull())
   
    
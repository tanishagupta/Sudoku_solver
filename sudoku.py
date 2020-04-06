board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
# The board has been taken randomly. It can be replaced with another board too. If the board is solvable, the solved board
# will be displayed otherwise the same board will be printed again. 

# The first function checks which places in the board are empty.
# The empty places have been shown using 0 (zero)
# The range is taken from 0 to 8 because the length of the board here is 9x9, hence we traverse through 9 boxes, both
# row-wise and column-wise
def empty(board):
    for i in range(0,9):  
        for j in range(0,9):  
            if board[i][j] == 0:  # if the position is empty then return that position
                return (i,j)
    return False

# The second function prints the 9x9 board on the screen
# The hyphen symbol (-) differentiates the rows in each of the 3x3 boxes while the tilde symbol (~) differentiates the 
# rows in each of the 9x9 boxes. The vertical bar (|) differentiates the columns throughout the board.

def prnt(board):
    for i in range(0,9): 
        if i%3 != 0: # To print the hypen symbol only at places which is not divisible by 3, so that rows are 
                     # differentiated in the 3x3 boxes
            print("------------------------------------")
        if i==3 or i==6:  # To print the tilde symbol only at positions at 3 or 6 in order to differentiate
                                     # the rows in 9x9 boxes
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for j in range(0,9):  
            if j==3 or j==6:  # To print the vertical bar in order to differentiate between each of the 3x3 boxes
                print("|",end="")
                
            if j == 8:  
                print(board[i][j])
            else:  
                print(board[i][j],"  ",end="")

# The third function checks whether the number entered at a particular position is valid or not.
# Here, 3 parameters are taken, namely the board which has to be solved, number which will be entered by the system
# itself and third is the position of the box.
def correct(board, number, position):
    
    # Checking validity for each row 
    for i in range(0,9): # Traversing through the board
        if board[position[0]][i] == number and position[1] != i: # If at position 0 i.e. row 1, if any one of the boxes 
                                                # contains a number which is equal to the number just entered by the system 
                                                # and if we are in a box in which the number was just entered, 
                                                # then that box won't be checked.
            return False
        
    # Checking validity for each column
    for i in range(0,9):
        if board[i][position[1]] ==  number and position[0] != i:  # Similarly, if at position 1 i.e. column 1, if any 
                                                  # one of the boxes contains a number which is equal to the number just 
                                                  # entered by the system and if we are in a box in which the number was 
                                                  # just entered then it won't be checked.
            return False
        
    # Checking validity for 3x3 boxes
    # Let's say that we are at row 0 and column 2, so 0//3 = 0 while 2//3 = 0. Hence this will give the result
    # that we are in row 0 of the first box from the 3x3 boxes.
    # Similarly, if we are at row 0 and column 3, so 0//3 = 0 while 3//3 = 1. Hence, this will give the result that
    # we are in row 0 of second box from the 3x3 boxes.
    # Again, if we are at row 6 and column 4, so 6//3 = 2 while 4//3 = 1. Hence, this will give the result that
    # we are in row 2 or box 1 from the 3x3 boxes.
    # This division is being multipied by 3 because every time, we will get the answer as 0,1 or two so if we want to
    # go to an index at 6 (for example), then we will multiply it by 3 and get there.
    box1 = ( position[0] // 3 )*3 
    box2 = ( position[1] // 3 )*3
    
    # Traversing the 9x9 box from 0 till the last element
    for i in range(box1, box1 + 3): 
        for j in range(box2, box2 + 3):
            if board[i][j] == number and (i,j) != position:   # If at a position, if any one of the boxes contains a number 
                                                    # which is equal to the number just entered by the system and if we are 
                                                    # in a box in which the number was just entered, then that box won't 
                                                    # be checked.
                return False
    return True

# The last function is used to solve the 9x9 board as a whole by making use of the 3 other functions made and discussed earlier.
# It contains one parameter i.e. the board.
# The function checks whether the board is empty or not, and then traverses through it to put the valid numbers in the
# correct boxes. If the numbers do not qualify the criteria of validity then, BACKTRACKING tackes place and the invalid
# positions are set to zero i.e. they are set to empty.
def sudoku(board):
    if not empty(board): # It means that if the 9x9 board is not empty anymore, then the board is solved and that we can 
                         # return True otherwise the empty() function returns some position where there are still empty boxes.
        return True
    else:
        row, col = empty(board)

    for i in range(1,10): # Looping through numbers 1 to 9 inorder for them to be filled in the board.
        if correct(board, i, (row, col)): # If the number entered by the system is valid/correct, then it will be placed at 
                                          # that position.
            board[row][col] = i

            if sudoku(board): # Here, the function sudoku() is called reccursively, to solve the board after saving the
                              # new valid values added to it recently. In this way, the whole board will be filled with valid
                              # numbers and can be solved.
                return True

            board[row][col] = 0 # Backtracking taking place if the board does not satisfy the criteria. It will set the 
                                # concerned positions to zero i.e. set them to empty so that new numbers can be tried.

    return False # Here, if the system is not able to solve the board, then backtracking will take place and it will go to
                 # the previous line and set the boxes with invalid numbers to zero.
 
    
    
prnt(board) # Calling the prnt() function to display the initial 9x9 board.
sudoku(board) # Calling the sudoku() function to solve the board.
print()
print("After solving the board, result is as follows:  ")
print()
prnt(board) # Again, calling the prnt() function to display the solved 9x9 board.

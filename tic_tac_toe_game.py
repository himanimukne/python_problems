#choose between X and O
marker='random'     #initialization
print("Welcome to this riveting tic tac toe game! \nMay the best player win!")
while marker != 'X' and marker != 'O':
    marker = input('Choose between X and O as your marker: ')     #keep asking for input till either X or O is received
    print(f"Player1 is to use {marker} in this game, and Player2, the opposite")
    
    
#game works only if user says it wants to continue. used as while loop condition later to run these functions iteratively
continue_playing='abc'     #initialization
while continue_playing != 'Y' and continue_playing != 'N':     #continue ahead only if Y
    continue_playing = input('Do you want to continue playing? Indicate with Y or N only: ')
        
        

#get input from user as to where to place their marker
def choose_position():
    acceptable_values=['1','2','3','4','5','6','7','8','9']    #since input returns string type, between 1-9
    global choice
    choice = 'wrong'   #initialization

    #ensure it is a number, and between 1-9 only, for a valid position
    while choice.isdigit()==False or choice not in acceptable_values:
        choice = input("Choose your next position (between 1 and 9 both inclusive): ")    
        if choice.isdigit()==False:    #to display error message if a number is not entered
            print("Error: Enter a valid digit.")
        if choice.isdigit()==True and choice not in acceptable_values:   #to display error message if digit is not in range
            print("Error: Enter number between 1 and 9 (inclusive) only.")
    
    global choice_int    #for using across functions 
    choice_int=int(choice)   #since input always returns string, cast it to integer to determine index position of board



#function to print board in a user-friendly way. this function will be called each time a marker is placed
def display_board(board):
    
    #ignore board[0], since for user convenience, position input is taken as 1-9
    print(board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])
    print('---------')
    print(board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print('---------')
    print(board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']     #initialization of board, which is a blank board



#this function helps place the right marker in the position (i.e. choice_int) chosen by the user
def place_marker(board,marker_value,choice_int):     #marker_value is toggled between X and O (later)
    board[choice_int]=marker_value        

    
    
#function to decide who wins, X or O
def who_wins():
    global win
    win=0    
    if board[1]==board[2]==board[3]=='X' or board[4]==board[5]==board[6]=='X' or board[7]==board[8]==board[9]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[3]==board[6]==board[9]=='X' or board[1]==board[5]==board[9]=='X' or board[3]==board[5]==board[7]=='X':
        print("Player with marker X wins!")
        win=1
    if board[1]==board[2]==board[3]=='O' or board[4]==board[5]==board[6]=='O' or board[7]==board[8]==board[9]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[3]==board[6]==board[9]=='O' or board[1]==board[5]==board[9]=='O' or board[3]==board[5]==board[7]=='O':
        print("Player with marker O wins!")
        win=1
    #if anyone wins, win=1, and this condition is used to come out of the loop
        

while continue_playing=='Y':
    
    global marker_value       #toggle marker_value between X and O
    for i in range(0,100000):
        if i%2==0:
            marker_value='X'
        if i%2==1:
            marker_value='O'
            
        choose_position()    
        place_marker(board,marker_value,choice_int)
        display_board(board)
        who_wins()       #call this at every instant to check if anyone won

        
        if win==1:     #implies someone won. break the loop
            print("Game over!")
            break
            
    break
    
    
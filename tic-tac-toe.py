import random
def marker():
    while True:
     marker1=input("Player 1 choose x or o")
     if marker1=='x':
        marker2='o'
        return(marker1,marker2)
     elif marker1=='o':
        marker2='x'
        return(marker1,marker2)
     else:
        print("enter valid marker")
board=[' ']*9
def printboard(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---|---|---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---|---|---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")
def position(board,marker, user):
    while True:
        if user == True:
            pos=int(input("enter your postion"))
        else:
            pos = random.randint(1,9)

        if pos in range(1,10):
            if board[pos-1]==' ':
                board[pos-1]=marker
                printboard(board)
                break
        else:
            print("Enter a valid position")

def check(board,marker):
    if ((board[0] ==marker and board[1]==marker and board[2]==marker) or 
        (board[3] ==marker and board[4] ==marker and board[5] == marker) or 
        (board[6] == marker and board[7] == marker and board[8] == marker) or 
        (board[0] == marker and board[3] == marker and board[6] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[0] == marker and board[4] == marker and board[8] == marker) or 
        (board[2] == marker and board[4] == marker and board[6] == marker)):
            return 'wins'

def play(user):
    player1,player2=marker()
    for i in range(0,9):
        print("player 1 enter your position:")
        position(board,player1,True)
        win=check(board,player1)
        if(win=='wins'):
            print("PLayer 1 wins!!")
            
            break
        print("player 2 enter your position:")
        position(board,player2,user)
        check(board,player2)
        if(win=='wins'):
            print("PLayer 2 wins!!")
            
            break
    if win !='wins':
        print('Its a draw')
def playagain():
     a=int(input("press 1 to play again or 2 to quit"))
     if(a==1):
      play()
     elif(a==2):
      print("Thanks for playing")

print("*****************************")
print("Welcome to Tic-Tac-Toe Game!!")
print("*****************************")
a = int(input("press 1 to play player vs computer or 2 to play player vs player"))
if(a == 1):
    play(False)
    playagain()
elif(a == 2):
    play(True)
    playagain()

 
 

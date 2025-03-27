import random
import copy

#Printing Board
def showboard():
    for h in range (4):
        for g in range (4):
            if board[h][g] == 0:
                board[h][g] = ' '
    print("",board[0][0],"","|","",board[0][1],"","|","",board[0][2],"","|","",board[0][3])
    print("--- + --- + --- + ---")
    print("",board[1][0],"","|","",board[1][1],"","|","",board[1][2],"","|","",board[1][3])
    print("--- + --- + --- + ---")
    print("",board[2][0],"","|","",board[2][1],"","|","",board[2][2],"","|","",board[2][3])
    print("--- + --- + --- + ---")
    print("",board[3][0],"","|","",board[3][1],"","|","",board[3][2],"","|","",board[3][3])

def checkifpossible():
                for h in range (4): #Visual only & deepcopy
                    for g in range (4):
                        if board[h][g] == ' ':
                            board[h][g] = 0
                        board[h][g]= int(board[h][g])
                tempboard2 = copy.deepcopy(board)
                for p in range (0,3): 
                    for j in range (3):
                        for k in range (4):
                            if j+1 != 4:
                                if tempboard2 [j][k] == 0:
                                        tempboard2 [j][k] = tempboard2[j+1][k]
                                        tempboard2 [j+1][k] = 0
                                else:
                                    if tempboard2[j][k] == tempboard2[j+1][k]:
                                        tempboard2[j][k] = tempboard2[j][k]*2
                                        tempboard2[j][k] = str(tempboard2[j][k])
                                        tempboard2[j+1][k] = 0
                for p in range (0,3):
                    for j in range (4):
                        for k in range (4):
                            if k+1 != 4:
                                if tempboard2 [j][k] == 0:
                                        tempboard2 [j][k] = tempboard2[j][k+1]
                                        tempboard2 [j][k+1] = 0
                                else:
                                    if tempboard2[j][k] == tempboard2 [j][k+1]:
                                        tempboard2[j][k] = tempboard2[j][k]*2
                                        tempboard2[j][k] = str(tempboard2[j][k])
                                        tempboard2[j][k+1] = 0
                for p in range (3):
                    for j in range (3,-1,-1):
                        for k in range (3,-1,-1):
                            if j-1 != -1:
                                if tempboard2 [j][k] == 0:
                                        tempboard2 [j][k] = tempboard2[j-1][k]
                                        tempboard2 [j-1][k] = 0
                                else:
                                    if tempboard2[j][k] == tempboard2 [j-1][k]:
                                        tempboard2[j][k] = tempboard2[j][k]*2
                                        tempboard2[j][k] = str(tempboard2[j][k])
                                        tempboard2[j-1][k] = 0
                for p in range (3):
                    for j in range (3,-1,-1):
                        for k in range (3,-1,-1):
                            if k-1 != -1:
                                if tempboard2 [j][k] == 0:
                                    tempboard2[j][k] = tempboard2[j][k-1]
                                    tempboard2[j][k-1] = 0
                                else:
                                    if tempboard2[j][k] == tempboard2 [j][k-1]:
                                        tempboard2[j][k] = tempboard2[j][k]*2
                                        tempboard2[j][k] = str(tempboard2[j][k])
                                        tempboard2[j][k-1] = 0
                if board == tempboard2:
                    return True
                return False                        
def playermove():
    global tempboard 
    move = 'none'
    k = 0
    j = 0
    v = 0
    while move!='w' and move!='a' and move!='s' and move!='d':
        move = input(print('Your move (w/a/s/d):'))
        if move!='w' and move!='a' and move!='s' and move!='d':
            print("That's an invalid move. Play again!")
    else:
        for h in range (4): #Visual only & deepcopy
            for g in range (4):
                if board[h][g] == ' ':
                        board[h][g] = 0
                board[h][g]= int(board[h][g])
        tempboard = copy.deepcopy(board)
        while tempboard == board:
            if v != 0: #Obriga a funcionar a partir da segunda vez do loop
                print("That's an invalid move. Play again!")
                move = input(print('Your move (w/a/s/d):'))
            if move == 'w':
                for p in range (0,3): #Jogada
                    for j in range (3):
                        for k in range (4):
                            if j+1 != 4:
                                if board [j][k] == 0:
                                        board [j][k] = board[j+1][k]
                                        board [j+1][k] = 0
                                else:
                                    if board[j][k] == board [j+1][k]:
                                        board[j][k] = board[j][k]*2
                                        board[j][k] = str(board[j][k])
                                        board[j+1][k] = 0
            if move == 'a':
                for p in range (0,3):
                    for j in range (4):
                        for k in range (4):
                            if k+1 != 4:
                                if board [j][k] == 0:
                                        board [j][k] = board[j][k+1]
                                        board [j][k+1] = 0
                                else:
                                    if board[j][k] == board [j][k+1]:
                                        board[j][k] = board[j][k]*2
                                        board[j][k] = str(board[j][k])
                                        board[j][k+1] = 0
            if move == 's':
                for p in range (3):
                    for j in range (3,-1,-1):
                        for k in range (3,-1,-1):
                            if j-1 != -1:
                                if board [j][k] == 0:
                                        board [j][k] = board[j-1][k]
                                        board [j-1][k] = 0
                                else:
                                    if board[j][k] == board [j-1][k]:
                                        board[j][k] = board[j][k]*2
                                        board[j][k] = str(board[j][k])
                                        board[j-1][k] = 0
            if move == 'd':
                for p in range (3):
                    for j in range (3,-1,-1):
                        for k in range (3,-1,-1):
                            if k-1 != -1:
                                if board [j][k] == 0:
                                    board [j][k] = board[j][k-1]
                                    board [j][k-1] = 0
                                else:
                                    if board[j][k] == board [j][k-1]:
                                        board[j][k] = board[j][k]*2
                                        board[j][k] = str(board[j][k])
                                        board[j][k-1] = 0
            v=v+1
            if tempboard != board:
                break

def wincheck():
    global win, lost 
    lost = False
    v=0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                win = True
            if board[i][j] != 0:
                v=v+1
                if v==16:
                    lost = True

tempboard=[
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ]
]

board=[
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ],
    [0 , 0 , 0 , 0 ]
]

#Game
win = False
row = col = 0
lost = False
gamestartposition1 = 0
gamestartposition2 = 0
o=0
pa = 's'
while pa == 's': #Apenas para reiniciar o jogo
    while win == False:
        i=0
        l=0
        while board[row][col] != 0 or i==0: # <-------------------------------
            i=i+1 #Obriga o programa a executar isto apenas 1 vez a cada ciclo
            newposition = random.randint(1,16)
            row, col = divmod(newposition-1,4)
            if o==0:
                l=l+1
                o=o+1
                while gamestartposition1 == gamestartposition2: #Apenas funciona 1 vez (inicio do jogo)
                    board=[
                        [0 , 0 , 0 , 0 ],
                        [0 , 0 , 0 , 0 ],
                        [0 , 0 , 0 , 0 ],
                        [0 , 0 , 0 , 0 ]
                    ]
                    gamestartposition1 = random.randint(1,16)
                    row, col = divmod(gamestartposition1-1,4)
                    chance = random.randint(1,10)
                    if chance >=7:
                        board[row][col] = 4
                    else:
                        board[row][col] = 2
                    gamestartposition2 = random.randint(1,16)
                    row, col = divmod(gamestartposition2-1,4)
                    chance = random.randint(1,10)
                    if chance >=7:
                        board[row][col] = 4
                    else:
                        board[row][col] = 2
        if l !=1: #Chance de ser 2 ou 4 a dar spawn.
            chance = random.randint(1,10)
            if chance == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
        showboard()
        if checkifpossible() == True:
            lost == True
            break
        playermove()
        wincheck()
        if lost == True and win == False:
            break
    if lost == True:
        pa = print('You lost! Do you want to play again?(s/n)')
    else:
        pa = input('You won! You reached 2048! Do you want to play again?(s/n)')

'''
A 3x3 tic-tac-toe game with an AI bot that runs using the minimax algorithm and alpha-beta pruning.
'''



'Prints out the gameboard'
def print_board():
    printy = ""
    for x in range(3):
        for y in range(3):
            if y < 2:
                printy = printy + board[x][y] + "|"
            else:
                printy = printy + board[x][y] + '\n'

        if x < 2:
            printy = printy + '-----' + '\n'
    return print(printy)

"Executes the players' moves on the board"
def player_turn(symbol,name):
    while game_won(board)[0] == False and board_full(board) == False:
        position = int(input(f"{name}, select a number [b/w 1 & 9] for your turn."))
        if position < 1 or position > 9:
            print("Input out of bounds! Select a number in range.")
            continue
        idx1 = int((position - 1) /3)
        idx2 = (position - 3*idx1) - 1
        if board[idx1][idx2] != ' ':
            print("Already Occupied!")
            continue
        else:
            board[idx1][idx2] = symbol
            break
        print_board()

"Checks if the game has been won by completing a horizontal row"
def horizontal_check(nboard):
    booly = False
    who_won = ' '
    for idx in range(3):
        if nboard[idx].count('X') == 3:
            booly = True
            who_won ='X'
            break
        elif nboard[idx].count('O') == 3:
            booly = True
            who_won = 'O'
            break
        else:
            continue
    return booly, who_won

"Checks if the game has been won by completing a vertical column"
def vertical_check(nboard):
    booly = False
    who_won = ' '
    for idx2 in range(3):
        O_count = 0
        X_count = 0
        for idx1 in range(3):
            if nboard[idx1][idx2] == 'O':
                O_count += 1
            elif nboard[idx1][idx2] == 'X':
                X_count += 1
        if X_count == 3:
            booly = True
            who_won = 'X'
        elif O_count == 3:
            booly = True
            who_won = 'O'
    return booly, who_won

"Checks if the game has been won by completing the forward diagonal"
def diagonal_check1(nboard):
    booly = False
    O_count = 0
    X_count = 0
    who_won = ' '
    for idx in range(3):
        if nboard[idx][idx] == 'X':
            X_count += 1
        elif nboard[idx][idx] == 'O':
            O_count += 1
    if X_count == 3:
        booly = True
        who_won = 'X'
    elif O_count == 3:
        booly = True
        who_won = 'O'
    return booly, who_won

"Checks if the game has been won by completing the backward diagonal"
def diagonal_check2(nboard):
    booly = False
    O_count = 0
    X_count = 0
    who_won = ' '
    idx1 = 0
    idx2 = 2
    for x in range(3):
        if nboard[idx1][idx2] == 'X':
            X_count += 1
        elif nboard[idx1][idx2] == 'O':
            O_count += 1
        idx1 += 1
        idx2 -= 1
    if X_count == 3:
        booly = True
        who_won = 'X'
    elif O_count == 3:
        booly = True
        who_won = 'O'
    return booly, who_won

"Checks if the board is full(no blank spaces remaining)"
def board_full(nboard):
    booly = True
    for idx1 in range(3):
        for idx2 in range(3):
            if nboard[idx1][idx2] != 'X' and nboard[idx1][idx2] != 'O':
                booly = False
                break
            else:
                continue
    return booly

"Using all the function checks if a game is won or not"
def game_won(nboard):
    booly = False
    winner = ''
    checkList = [horizontal_check(nboard),vertical_check(nboard), diagonal_check1(nboard), diagonal_check2(nboard)]
    for check in checkList:
        if check[0] is True:
            booly = True
            winner = check[1]
    return booly, winner

'''Generates a list of all the possible moves remaining for a
player at any point in the game'''
def possible_moves(nboard):
    possible_pos = []
    for idx1 in range(3):
        for idx2 in range(3):
            if nboard[idx1][idx2] == ' ':
                possible_pos.append((idx1,idx2))
    return possible_pos

import copy

'The minimax algorithm using alpha-beta pruning'
alpha = -1000000
beta = 1000000
def some_try1(nboard, player,alpha, beta):
    orig = copy.deepcopy(nboard)
    if game_won(orig)[0]:
            if game_won(orig)[1] == p1_sym:
                return -10,None
            else:
                return 10,None
    elif board_full(orig):
            return 0,None
    if player == cpu_sym:
        best_move = (-20,None)
        for move in possible_moves(nboard):
            orig[move[0]][move[1]] = cpu_sym
            val = some_try1(orig,p1_sym,alpha,beta)[0]
            orig[move[0]][move[1]] = ' '
            if val > best_move[0]:
                best_move = (val,move)
            if val > alpha:
                alpha = val
            if val >= beta:
                break
        return best_move
    elif player == p1_sym:
        best_move = (20,None)
        for move in possible_moves(nboard):
            orig[move[0]][move[1]] = p1_sym
            val = some_try1(orig,cpu_sym,alpha,beta)[0]
            orig[move[0]][move[1]] = ' '
            if val < best_move[0]:
                best_move = (val,move)
            if val < beta:
                beta = val
            if val <= alpha:
                break
        return best_move

'The minimax algorithm'
def some_try(nboard, player):
    orig = copy.deepcopy(nboard)
    if game_won(orig)[0]:
            if game_won(orig)[1] == p1_sym:
                return -10,None
            else:
                return 10,None
    elif board_full(orig):
            return 0,None
    if player == cpu_sym:
        best_move = (-20,None)
        for move in possible_moves(nboard):
            orig[move[0]][move[1]] = cpu_sym
            val= some_try(orig,p1_sym)[0]
            orig[move[0]][move[1]] = ' '
            if val > best_move[0]:
                best_move = (val,move)
        return best_move
    elif player == p1_sym:
        best_move = (20,None)
        for move in possible_moves(nboard):
            orig[move[0]][move[1]] = p1_sym
            val = some_try(orig,cpu_sym)[0]
            orig[move[0]][move[1]] = ' '
            if val < best_move[0]:
                best_move = (val,move)
        return best_move
"Implementing the minimax algorithm"
def play_minimax(nboard):
    if game_won(board)[0] == False and board_full(board) == False:
        turn = some_try1(nboard,cpu_sym,alpha, beta)
        board[turn[1][0]][turn[1][1]] = cpu_sym
        print_board()
    else:
        pass

"A helper function to display who has won the game"
def disp_winner(nboard):
    if game_won(nboard)[0]:
        print(f"Congratulations {game_won(nboard)[1]}, you won!")
    elif board_full(nboard):
        print("Game Tied!")

"Implementation of the tic-tac-toe game, run until user quits."
import random
print("Welcome to Tic Tac Toe by Furrukh Asif")
p1_name = input("Player, enter your name: ")
while True:
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    X_count = 0
    O_count = 0
    who_won = ' '
    cpu_name = 'cpu'
    p1_sym = ' '
    cpu_sym = 'O'
    dec = input("Are you ready to play? ('Yes' to play, 'No' to quit)")
    if dec.strip().upper() == 'YES':
            x = random.random() < 0.5
            sym = input(f"{p1_name}, choose your symbol, 'X' or 'O'")
            while True:
                if sym.strip().upper() == 'X':
                    p1_sym = 'X'
                    cpu_sym = 'O'
                    break
                elif sym.strip().upper() == 'O':
                    p1_sym = 'O'
                    cpu_sym = 'X'
                    break
                else:
                    print("Invalid Input! Please choose a valid symbol.")
            if x:
                print(f"{p1_name}, you will go first.")
                print_board()
                while game_won(board)[0] == False and board_full(board) == False:
                    player_turn(p1_sym,p1_name)
                    play_minimax(board)
                disp_winner(board)
            else:
                print(f"{cpu_name}, you will go first.")
                print_board()
                while game_won(board)[0] == False and board_full(board) == False:
                    play_minimax(board)
                    player_turn(p1_sym,p1_name)
                disp_winner(board)
    elif dec.strip().upper() == 'NO':
        break
    else:
        print("Invalid Input")

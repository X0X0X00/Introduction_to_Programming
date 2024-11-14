"""
week 12 - live coding example
mkp
"""
import random
from graphics import *

class Board:
    def __init__(self):
        self.gameboard = []
        self.gameboard.append([' ' , ' ' , ' ' ])
        self.gameboard.append([' ' , ' ' , ' ' ])
        self.gameboard.append([' ' , ' ' , ' ' ])
        self.turns = 0

    def get_gameboard(self):
        return self.gameboard

    def get_turns(self):
        return self.turns

    def show_board(self):
        print(self.gameboard[0])
        print(self.gameboard[1])
        print(self.gameboard[2])


def comp_move(board):
    print('Computer moves')
    row = random.randint(0,2)
    col = random.randint(0,2)
    while board.gameboard[row][col] != ' ':
        row = random.randint(0,2)
        col = random.randint(0,2)
    board.gameboard[row][col] = 'X'
    board.turns += 1
    board.show_board()
    
    
    

def player_move(board):
    print('Player moves')
    row = int(input('Row: '))
    col = int(input('Col: '))
    while board.gameboard[row][col] != ' ':
        row = int(input('Row: '))
        col = int(input('Col: '))
    board.gameboard[row][col] = 'O'
    board.turns += 1
    board.show_board()

def play(board):
    while (board.get_turns() < 9):
        comp_move(board) # comp move
        if check_win(board, 'X'):
            print('You lose')
            break
        if board.get_turns()==9:
            print('Tie')
            return
        player_move(board)
        if check_win(board, 'O'):
            print('You win')
            break
    if board.get_turns()==9:
        print('Tie')
        
        
def check_win(board, ch):
    g_board = board.gameboard
    if g_board[0][0] == g_board[0][1] == g_board[0][2] == ch:
        return True
    elif g_board[1][0] == g_board[1][1] == g_board[1][2] == ch:
        return True
    elif g_board[2][0] == g_board[2][1] == g_board[2][2] == ch:
        return True
    elif g_board[0][0] == g_board[1][0] == g_board[2][0] == ch:
        return True
    elif g_board[0][1] == g_board[1][1] == g_board[1][2] == ch:
        return True
    elif g_board[0][2] == g_board[2][1] == g_board[2][2] == ch:
        return True
    elif g_board[0][0] == g_board[1][1] == g_board[2][2] == ch:
        return True
    elif g_board[0][2] == g_board[1][1] == g_board[2][0] == ch:
        return True
    return False

def draw_board(board):
    win = GraphWin( "TicTacToe",300 , 300 )
    rect = Rectangle(Point(0,0),Point(300,300))
    rect.draw(win)
    Line(Point(100,0),Point(100,300)).draw(win)
    Line(Point(200,0),Point(200,300)).draw(win)
    Line(Point(0,100),Point(300,100)).draw(win)
    Line(Point(0,200),Point(300,200)).draw(win)
    rect.setFill('SkyBlue')
    label = Text(Point(150,150), ' ')
    label.draw(win)
    for i in range(3):
        for j in range(3):
            if board.gameboard[j][i] == 'X':
                Text(Point(i*100+50,j*100+50), 'X').draw(win)
            elif board.gameboard[j][i] == 'O':
                Text(Point(i*100+50,j*100+50), 'O').draw(win)

if __name__=='__main__':
    board = Board()
    board.show_board()
    play(board)
    draw_board(board)



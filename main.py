import pygame
from math import floor

WIDTH = 300
LENGTH = 300
row = 3
column = 3
RAD = WIDTH//column
win_condition = 3
turn = 1
played_turns = 0
state = 1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


pygame.init()
scr = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("tic tac toe")

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

X = pygame.transform.scale(pygame.image.load("x.png"), (floor(RAD*0.7), floor(RAD*0.7)))
O = pygame.transform.scale(pygame.image.load("o.png"), (floor(RAD*0.7), floor(RAD*0.7)))
SHAPE_X = (X.get_width(), X.get_height())
SHAPE_O = (O.get_width(), O.get_height())


def win(cord):
    i = cord[0]
    j = cord[1]
    mark = board[i][j]
    if mark == 0 or played_turns < win_condition*2-1:
        return False

    #horizontal
    counter = 0
    p = j
    while p < row and board[i][p] == mark and counter != win_condition:
        p+=1
        counter+=1

    p = j - 1
    while 0 <= p and board[i][p] == mark and counter != win_condition:
        p -= 1
        counter += 1
    
    if counter == win_condition:
        return True
    
    #vertical
    counter = 0
    p = i
    while p < column and board[p][j] == mark and counter != win_condition:
        p += 1
        counter += 1

    p = i - 1
    while 0 <= p and board[p][j] == mark and counter != win_condition:
        p -= 1
        counter += 1

    if counter == win_condition:
        return True

    #diagonal_1
    counter = 0
    p_1 = i
    p_2 = j
    while p_2 < row and p_1 < column  and board[p_1][p_2] == mark and counter != win_condition:
        p_1 += 1
        p_2 += 1
        counter += 1

    p_1 = i - 1
    p_2 = j - 1
    while 0 <= p_2 and 0 <= p_1 and board[p_1][p_2] == mark and counter != win_condition:
        p_1 -= 1
        p_2 -= 1
        counter += 1

    if counter == win_condition:
        return True

    #diagonal_2
    counter = 0
    p_1 = i
    p_2 = j
    while 0 <= p_2 and p_1 < column and board[p_1][p_2] == mark and counter != win_condition:
        p_1 += 1
        p_2 -= 1
        counter += 1

    p_1 = i - 1
    p_2 = j + 1
    while p_2 < row and 0 <= p_1 and board[p_1][p_2] == mark and counter != win_condition:
        p_1 -= 1
        p_2 += 1
        counter += 1

    if counter == win_condition:
        return True

    return False


def draw_board():
    scr.fill(WHITE)
    border = 3

    for i in range(column-1):
        pygame.draw.line(scr, BLACK, (RAD*(i+1), 0), (RAD*(i+1), LENGTH), border)
    for i in range(row-1):
        pygame.draw.line(scr, BLACK, (0, RAD*(i+1)), (WIDTH, RAD*(i+1)), border)


def lmb_click():
    global turn
    if state == 1:
        pos = pygame.mouse.get_pos()
        i = pos[1]//RAD
        j = pos[0]//RAD
        if board[i][j]:
            return False
        if turn == 1:
            board[i][j] = 1
            turn = 2
        else:
            board[i][j] = 2
            turn = 1
        return (i, j)


def update_board(cord):
    y = cord[0]*RAD + (RAD-X.get_width())//2
    x = cord[1]*RAD + (RAD-X.get_height())//2

    if board[cord[0]][cord[1]] == 1:
        scr.blit(X, (x, y))
    else:
        scr.blit(O, (x, y))
    return


def main():
    global played_turns
    scr.fill(WHITE)
    draw_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                    cord = lmb_click()
                    if cord:
                        played_turns += 1
                        update_board(cord)
                        if win(cord):
                            print(str(turn)+" lost")



        pygame.display.update()


if __name__ == "__main__":
    main()
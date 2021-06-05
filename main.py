import pygame
import sys
from math import floor

RAD = 100
ROWS = 4
COLUMNS = 4
WIN_CONDITION = 3
WIDTH = COLUMNS * RAD
HEIGHT = ROWS * RAD
TURN = 1
PLAYED_TURNS = 0
STATE = 1
BOARD = [[0] * COLUMNS for i in range(ROWS)]

pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tic tac toe")

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
X = pygame.transform.scale(pygame.image.load("x.png"), (floor(RAD*0.7), floor(RAD*0.7)))
O = pygame.transform.scale(pygame.image.load("o.png"), (floor(RAD*0.7), floor(RAD*0.7)))


def win(cord):
    i = cord[0]
    j = cord[1]
    mark = BOARD[i][j]
    if mark == 0 or PLAYED_TURNS < WIN_CONDITION*2-1:
        return False

    #horizontal
    counter = 0
    p = j
    while p < ROWS and BOARD[i][p] == mark and counter != WIN_CONDITION:
        p+=1
        counter+=1

    p = j - 1
    while 0 <= p and BOARD[i][p] == mark and counter != WIN_CONDITION:
        p -= 1
        counter += 1
    
    if counter == WIN_CONDITION:
        return True
    
    #vertical
    counter = 0
    p = i
    while p < COLUMNS and BOARD[p][j] == mark and counter != WIN_CONDITION:
        p += 1
        counter += 1

    p = i - 1
    while 0 <= p and BOARD[p][j] == mark and counter != WIN_CONDITION:
        p -= 1
        counter += 1

    if counter == WIN_CONDITION:
        return True

    #diagonal_1
    counter = 0
    p_1 = i
    p_2 = j
    while p_2 < ROWS and p_1 < COLUMNS  and BOARD[p_1][p_2] == mark and counter != WIN_CONDITION:
        p_1 += 1
        p_2 += 1
        counter += 1

    p_1 = i - 1
    p_2 = j - 1
    while 0 <= p_2 and 0 <= p_1 and BOARD[p_1][p_2] == mark and counter != WIN_CONDITION:
        p_1 -= 1
        p_2 -= 1
        counter += 1

    if counter == WIN_CONDITION:
        return True

    #diagonal_2
    counter = 0
    p_1 = i
    p_2 = j
    while 0 <= p_2 and p_1 < COLUMNS and BOARD[p_1][p_2] == mark and counter != WIN_CONDITION:
        p_1 += 1
        p_2 -= 1
        counter += 1

    p_1 = i - 1
    p_2 = j + 1
    while p_2 < ROWS and 0 <= p_1 and BOARD[p_1][p_2] == mark and counter != WIN_CONDITION:
        p_1 -= 1
        p_2 += 1
        counter += 1

    if counter == WIN_CONDITION:
        return True

    return False


def draw_board():
    scr.fill(WHITE)
    border = 3

    for i in range(COLUMNS - 1):
        pygame.draw.line(scr, BLACK, (RAD*(i+1), 0), (RAD * (i+1), HEIGHT), border)
    for i in range(ROWS - 1):
        pygame.draw.line(scr, BLACK, (0, RAD*(i+1)), (WIDTH, RAD*(i+1)), border)


def lmb_click():
    global TURN
    if STATE == 1:
        pos = pygame.mouse.get_pos()
        i = pos[1]//RAD
        j = pos[0]//RAD
        if BOARD[i][j]:
            return False
        if TURN == 1:
            BOARD[i][j] = 1
            TURN = 2
        else:
            BOARD[i][j] = 2
            TURN = 1
        return (i, j)


def update_board(cord):
    y = cord[0]*RAD + (RAD-X.get_width())//2
    x = cord[1]*RAD + (RAD-X.get_height())//2

    if BOARD[cord[0]][cord[1]] == 1:
        scr.blit(X, (x, y))
    else:
        scr.blit(O, (x, y))
    return


def reset():
    global BOARD, PLAYED_TURNS, TURN
    PLAYED_TURNS = 0
    TURN = 1
    draw_board()
    BOARD = [[0] * COLUMNS for i in range(ROWS)]


def wait(t):
    x = pygame.time.get_ticks()
    while pygame.time.get_ticks() < x +t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def main():
    global PLAYED_TURNS
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
                        PLAYED_TURNS += 1
                        update_board(cord)
                        if win(cord):
                            pygame.display.update()
                            if TURN == 1:
                                end_scr = font.render("O won!", True, BLACK)
                            else:
                                end_scr = font.render("X won!", True, BLACK)
                            wait(650)
                            scr.fill(WHITE)
                            dest = ((WIDTH - end_scr.get_width())//2, (HEIGHT - end_scr.get_height())//2)
                            scr.blit(end_scr, dest)
                            pygame.display.update()
                            wait(1300)
                            reset()


        pygame.display.update()


if __name__ == "__main__":
    main()
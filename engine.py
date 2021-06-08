import pygame
import sys


class Engine():
    def __init__(self, rows=3, columns=3, rad=100, win_condition=3):
        self.rad = rad
        self.columns = columns
        self.rows = rows
        self.win_condition = win_condition
        self.width = columns * rad
        self.height = rows * rad
        self.turn = 1
        self.played_turns = 0
        self.state = 1
        self.border = 3
        self.board = [[0] * columns for i in range(rows)]

        self.scr = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("tic tac toe")

        self.WHITE = pygame.Color(255, 255, 255)
        self.BLACK = pygame.Color(0, 0, 0)

        self.font = pygame.font.SysFont("Verdana", 60)
        self.X = pygame.transform.scale(pygame.image.load("x.png"), (int(rad*0.7), int(rad*0.7)))
        self.O = pygame.transform.scale(pygame.image.load("o.png"), (int(rad*0.7), int(rad*0.7)))

    def win_check(self, cord):
        i = cord[0]
        j = cord[1]
        mark = self.board[i][j]
        if mark == 0 or self.played_turns < self.win_condition*2-1:
            return False

        #horizontal
        counter = 0
        p = j
        while p < self.rows and self.board[i][p] == mark and counter != self.win_condition:
            p+=1
            counter+=1

        p = j - 1
        while 0 <= p and self.board[i][p] == mark and counter != self.win_condition:
            p -= 1
            counter += 1

        if counter == self.win_condition:
            return True

        #vertical
        counter = 0
        p = i
        while p < self.columns and self.board[p][j] == mark and counter != self.win_condition:
            p += 1
            counter += 1

        p = i - 1
        while 0 <= p and self.board[p][j] == mark and counter != self.win_condition:
            p -= 1
            counter += 1

        if counter == self.win_condition:
            return True

        #diagonal_1
        counter = 0
        p_1 = i
        p_2 = j
        while p_2 < self.rows and p_1 < self.columns  and self.board[p_1][p_2] == mark and counter != self.win_condition:
            p_1 += 1
            p_2 += 1
            counter += 1

        p_1 = i - 1
        p_2 = j - 1
        while 0 <= p_2 and 0 <= p_1 and self.board[p_1][p_2] == mark and counter != self.win_condition:
            p_1 -= 1
            p_2 -= 1
            counter += 1

        if counter == self.win_condition:
            return True

        #diagonal_2
        counter = 0
        p_1 = i
        p_2 = j
        while 0 <= p_2 and p_1 < self.columns and self.board[p_1][p_2] == mark and counter != self.win_condition:
            p_1 += 1
            p_2 -= 1
            counter += 1

        p_1 = i - 1
        p_2 = j + 1
        while p_2 < self.rows and 0 <= p_1 and self.board[p_1][p_2] == mark and counter != self.win_condition:
            p_1 -= 1
            p_2 += 1
            counter += 1

        if counter == self.win_condition:
            return True

        return False

    def draw_board(self):
        self.scr.fill(self.WHITE)
        for i in range(self.columns - 1):
            pygame.draw.line(self.scr, self.BLACK, (self.rad*(i+1), 0), (self.rad * (i+1), self.height), self.border)
        for i in range(self.rows - 1):
            pygame.draw.line(self.scr, self.BLACK, (0, self.rad*(i+1)), (self.width, self.rad*(i+1)), self.border)

    def lmb_click(self):
        if self.state == 1:
            pos = pygame.mouse.get_pos()
            j = pos[0]//self.rad
            i = pos[1]//self.rad
            if self.board[i][j]:
                return False
            if self.turn == 1:
                self.board[i][j] = 1
                self.turn = 2
            else:
                self.board[i][j] = 2
                self.turn = 1
            return (i, j)

    def update_board(self, cord):
        x = cord[1]*self.rad + (self.rad-self.X.get_height())//2
        y = cord[0]*self.rad + (self.rad-self.X.get_width())//2

        if self.board[cord[0]][cord[1]] == 1:
            self.scr.blit(self.X, (x, y))
        else:
            self.scr.blit(self.O, (x, y))
        return

    def reset(self):
        self.played_turns = 0
        self.turn = 1
        self.draw_board()
        self.board = [[0] * self.columns for i in range(self.rows)]

    @staticmethod
    def wait(t):
        x = pygame.time.get_ticks()
        while pygame.time.get_ticks() < x +t:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def draw(self):
        pygame.display.update()
        end_scr = self.font.render("Draw!", True, self.BLACK)
        self.wait(650)
        self.scr.fill(self.WHITE)
        destination = ((self.width - end_scr.get_width())//2, (self.height - end_scr.get_height())//2)
        self.scr.blit(end_scr, destination)
        pygame.display.update()
        self.wait(1300)
        self.reset()

    def win(self):
        pygame.display.update()
        if self.turn == 1:
            end_scr = self.font.render("O win!", True, self.BLACK)
        else:
            end_scr = self.font.render("X win!", True, self.BLACK)
        self.wait(650)
        self.scr.fill(self.WHITE)
        destination = ((self.width - end_scr.get_width())//2, (self.height - end_scr.get_height())//2)
        self.scr.blit(end_scr, destination)
        pygame.display.update()
        self.wait(1300)
        self.reset()

    def start(self):
        self.draw_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == 1:
                        cord = self.lmb_click()
                        if cord:
                            self.played_turns += 1
                            self.update_board(cord)
                            if self.played_turns == self.rows * self.columns:
                                self.draw()
                            elif self.win_check(cord):
                                self.win()


            pygame.display.update()
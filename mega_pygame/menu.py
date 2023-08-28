# import libraries
import sys
import pygame as pg
from game_file import Button, tic_tac_toe
from runtimes import ttt_runtime

# starting home screen
pg.init()
size = width, height = 600, 600
screen = pg.display.set_mode(size)
WHITE = (255, 255, 255)
screen.fill(WHITE)
pg.display.set_caption("Menu")

# tictactoe button 
tt_location = (25, 50)
tictactoe = Button("tictactoeboard.png", tic_tac_toe)
smaller_tt = pg.transform.scale(tictactoe.get_image(), (50, 40))
t_rect = smaller_tt.get_rect(topleft = tt_location)
screen.blit(smaller_tt, tt_location)

# Game Title
font = pg.font.Font('freesansbold.ttf', 20)
text = font.render('KJs Collection', True, (0, 0, 0), WHITE)
screen.blit(text, (230, 290))
pg.display.flip()

# Menu Runtime
break_flag = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if t_rect.collidepoint(pos):
                ttt_runtime(screen)
                break_flag = True
                break
    if break_flag: break
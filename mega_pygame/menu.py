# import libraries
import sys
import pygame as pg
from game_file import Button, tic_tac_toe

# starting home screen
pg.init()
size = width, height = 600, 600
screen = pg.display.set_mode(size)
WHITE = (255, 255, 255)
screen.fill(WHITE)
pg.display.set_caption("Menu")

# tictactoe Game


# tictactoe button 
tictac_location = (25, 50)
tictactoe = Button("tictactoeboard.png")
smaller_tictac = pg.transform.scale(tictactoe.get_image(), (50, 40))
t_rect = smaller_tictac.get_rect(topleft = tictac_location)
screen.blit(smaller_tictac, tictac_location)



# Game Title
font = pg.font.Font('freesansbold.ttf', 20)
text = font.render('KJs Collection', True, (0, 0, 0), WHITE)
screen.blit(text, (230, 290))
pg.display.flip()

# Menu Runtime
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if t_rect.collidepoint(pos):
                tictactoe.switch_scene(screen)
                exit(0)
                break
import sys
import pygame as pg
from game_button_file import game_button

pg.init()
size = width, height = 600, 600
screen = pg.display.set_mode(size)
screen = screen.fill((255, 255, 255))
pg.display.set_caption("Menu")

tictactoe = game_button("tictactoeboard.png", screen)
t = screen.blit(tictactoe.get_image(), (25, 50))

font = pg.font.Font('freesansbold.ttf', 20)
text = font.render('KJs Collection', True, (255, 0, 0), (0, 75, 0))
screen.blit(text, (250, 250))
pg.display.flip()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos
            if t.collidepoint(pos):
                tictactoe.switch_scene()
                break
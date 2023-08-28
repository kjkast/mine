# import libraries
import sys
import pygame as pg
from game_file import tic_tac_toe

def ttt_runtime(screen) -> None:
    instance = tic_tac_toe(screen)
    instance.start_game()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
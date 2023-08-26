import pygame as pg

class Game:

    def __init__(self, background):
        self.background = background
        return
    
    def switch_scene(self, screen):
        WHITE = (255, 255, 255) 
        screen.fill(WHITE)
        return
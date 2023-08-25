import pygame as pg

class game_button:
    def __init__(self, file_name, screen):
        self.image = pg.image.load(file_name).convert()
        self.screen = screen
        return

    def get_image(self):
        return self.image



        
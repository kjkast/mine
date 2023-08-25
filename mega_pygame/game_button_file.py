import pygame as pg

class game_button:
    
    

    def __init__(self, file_name, screen):
        self.image = pg.Surface.convert(pg.image.load(file_name))
        self.screen = screen
        return

    def get_image(self):
        return self.image

    def switch_scene(self):
        self.screen.fill((255, 255, 255))
        return

    def update_location(self):
        return
        
import pygame as pg
from abc import ABC, abstractmethod
from ast import literal_eval

class Game(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

# to choose game in the Menu scene
class Button:

    def __init__(self, file_name, game: Game):
        self.image = pg.image.load(file_name).convert()
        self.game = game
        return

    # returns image as a Surface
    def get_image(self):
        return self.image
    
    # 
    def switch_scene(self, screen):
        self.game.start_game(screen)
        return

# start of games

class tic_tac_toe(Game):

    def __init__(self):
        super().__init__()
        self.score = 0
    
    def start_game(self, screen):
        WHITE = (255, 255, 255) 
        screen.fill(WHITE)

    def read_score(self) -> list:
        with open("scores.txt", "r") as file:
            for line in file:
                if line.startswith("tictactoe: "):
                    return literal_eval(line[len("tictactoe: "):].strip())
                
    def save_score(self, score: list):
        updated_lines = []
        with open("scores.txt", "w") as file:
            for line in file:
                if line.startswith("tictactoe: "):
                    updated_lines.append(f"tictactoe: {score}\n")
                else:
                    updated_lines.append(line)
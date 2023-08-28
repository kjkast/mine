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

    def __init__(self, file_name, game) -> None:
        self.image = pg.image.load(file_name).convert()
        self.game = game

    # returns image as a Surface
    def get_image(self):
        return self.image
    
    def switch_scene(self, screen) -> None:
        self.game.start_game()

# start of games

class tic_tac_toe(Game):

    def __init__(self, screen):
        super().__init__()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.ai = False
        self.screen = screen
    
    def start_game(self) -> None:
        WHITE = (255, 255, 255) 
        self.screen.fill(WHITE)
        pg.display.set_caption("TicTacToe")
        background = pg.image.load("tictactoeboard.png").convert()
        background = pg.transform.scale(background, (510, 394))
        self.screen.blit(background, (50, 100))
        pg.display.flip()

    def read_score(self) -> list:
        with open("scores.txt", "r") as file:
            for line in file:
                if line.startswith("tictactoe: "):
                    return literal_eval(line[len("tictactoe: "):].strip())
                
    def save_score(self, score: list) -> None:
        updated_lines = []
        with open("scores.txt", "r") as file:
            for line in file:
                if line.startswith("tictactoe: "):
                    updated_lines.append(f"tictactoe: {score}\n")
                else:
                    updated_lines.append(line)
        with open("scores.txt", "w"):
            for line in file:
                file.writelines(updated_lines)

    def place_xo(self, position, is_x):
        pass

    def activate_ai(self) -> None:
        self.ai = True
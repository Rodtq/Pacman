import pygame

from PacMan import movementConstants
from PacMan.movable import MovableObserver
from PacMan.movementConstants import MovementConstants
from PacMan.colorConstants import ColorConstants
from PacMan.gameElement import GameElement
import random


class Ghost(GameElement, MovableObserver):
    def __init__(self, color, size):
        self.column = 13
        self.row = 15
        self.size = size
        self.color = color
        self.velocity = 1
        self.direction = MovementConstants.DOWN
        self.column_intention = self.column
        self.row_intention = self.row

    def draw(self, game_screen):
        piece = self.size // 8
        px = int(self.column * self.size)
        py = int(self.row * self.size)
        outline = [(px, py + self.size),
                   (px + piece, py + piece * 2),
                   (px + piece * 2, py + piece * 2),
                   (px + piece * 3, py),
                   (px + piece * 4, py),
                   (px + piece * 5, py),
                   (px + piece * 6, py + piece // 2),
                   (px + piece * 7, py + piece * 2),
                   (px + self.size, py + self.size)]
        pygame.draw.polygon(game_screen, self.color, outline, 0)
        eye_radius_ext = piece
        eye_radius_int = piece // 2

        eye_e_x = int(px + piece * 2.5)
        eye_e_y = int(py + piece * 2.5)
        eye_d_x = int(px + piece * 5.5)
        eye_d_y = int(py + piece * 2.5)

        pygame.draw.circle(game_screen, ColorConstants.WHITE, (eye_e_x, eye_e_y), eye_radius_ext, 0)
        pygame.draw.circle(game_screen, ColorConstants.BLACK, (eye_e_x, eye_e_y), eye_radius_int, 0)
        pygame.draw.circle(game_screen, ColorConstants.WHITE, (eye_d_x, eye_d_y), eye_radius_ext, 0)
        pygame.draw.circle(game_screen, ColorConstants.BLACK, (eye_d_x, eye_d_y), eye_radius_int, 0)

    def event_processor(self, events):
        pass

    def rules_calculator(self):
        if self.direction == MovementConstants.UP:
            self.row_intention -= self.velocity
        if self.direction == MovementConstants.DOWN:
            self.row_intention += self.velocity
        if self.direction == MovementConstants.LEFT:
            self.column_intention -= self.velocity
        if self.direction == MovementConstants.RIGHT:
            self.column_intention += self.velocity

    def crossroad(self, directions):
        self.change_direction(directions)

    def accept_movement(self):
        self.column = self.column_intention
        self.row = self.row_intention

    def refuse_movement(self, directions):
        self.column_intention = self.column
        self.row_intention = self.row
        self.change_direction(directions)

    def change_direction(self, directions):
        self.direction = random.choice(directions)

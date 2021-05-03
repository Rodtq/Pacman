import pygame

from PacMan.gameElement import GameElement
from PacMan.colorConstants import ColorConstants
from PacMan.movable import MovableObserver


class Hero(GameElement, MovableObserver):
    def __init__(self, column_size):
        self.character_primary_color = ColorConstants.YELLOW
        self.__character_secondary_color = ColorConstants.BLACK
        self.row = 1
        self.column = 1
        self.__character_x_center = 400
        self.__character_y_center = 300
        self.__character_size = column_size
        self.__character_speed_x = 0
        self.__character_speed_y = 0
        self.__character_size_radius = self.__character_size // 2
        self.column_intention = self.column
        self.row_intention = self.row
        self.mouth_open = 0
        self.mouth_open_velocity = 1
        self.lifes = 3
        self.hero_img = 0

    def rules_calculator(self):
        # calcula movimentação do personagem com relação a velocidade em x e y
        self.column_intention = self.column + self.__character_speed_x
        self.row_intention = self.row + self.__character_speed_y
        self.__character_x_center = int(self.column * self.__character_size + self.__character_size_radius)
        self.__character_y_center = int(self.row * self.__character_size + self.__character_size_radius)

    def draw(self, game_screen):
        # draw body

        self.hero_img = pygame.draw.circle(game_screen, self.character_primary_color,
                           (self.__character_x_center, self.__character_y_center),
                           self.__character_size_radius, 0)

        self.mouth_open += self.mouth_open_velocity
        if self.mouth_open >= self.__character_size_radius:
            self.mouth_open_velocity = -1
        if self.mouth_open <= 0:
            self.mouth_open_velocity = 1

        # draw mouth
        # Desenho da boca do Pacman
        mouth_corner = (self.__character_x_center, self.__character_y_center)
        upper_lip = (self.__character_x_center + self.__character_size_radius,
                     self.__character_y_center - self.mouth_open)
        lower_lip = (self.__character_x_center + self.__character_size_radius,
                     self.__character_y_center + self.mouth_open)
        mouth_coordinates = [mouth_corner, upper_lip, lower_lip]
        pygame.draw.polygon(game_screen, self.__character_secondary_color, mouth_coordinates, 0)

        # draw eye
        eye_x = int(self.__character_x_center + self.__character_size_radius / 3)
        eye_y = int(self.__character_y_center - self.__character_size_radius * 0.70)
        eye_radius = self.__character_size_radius / 10
        pygame.draw.circle(game_screen, self.__character_secondary_color, (eye_x, eye_y), eye_radius, 0)

    def event_processor(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.__character_speed_x = 1
                elif e.key == pygame.K_LEFT:
                    self.__character_speed_x = -1
                elif e.key == pygame.K_UP:
                    self.__character_speed_y = -1
                elif e.key == pygame.K_DOWN:
                    self.__character_speed_y = 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.__character_speed_x = 0
                elif e.key == pygame.K_LEFT:
                    self.__character_speed_x = 0
                if e.key == pygame.K_UP:
                    self.__character_speed_y = 0
                elif e.key == pygame.K_DOWN:
                    self.__character_speed_y = 0

    def accept_movement(self):
        self.column = self.column_intention
        self.row = self.row_intention

    def refuse_movement(self, directions):
        self.column_intention = self.column
        self.row_intention = self.row

    def crossroad(self, directions):
        pass

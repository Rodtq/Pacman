import PacMan.hero
from PacMan.gameElement import GameElement
import pygame
from PacMan.movableSubject import MovableSubject
from PacMan.colorConstants import ColorConstants
from PacMan.movementConstants import MovementConstants
from PacMan.gameStatesConstants import GameStateConstants


class Scenery(GameElement, MovableSubject):

    def __init__(self, game_screen) -> None:
        self.game_state = GameStateConstants.Running
        self.__game_screen = game_screen
        self.__column_size = self.__game_screen.column_size
        self.hero = 0
        self.movables = []
        self.font = pygame.font.SysFont("arial", 24, True, False)
        self.__tile_color = ColorConstants.BLUE
        self.__path_color = ColorConstants.BLACK
        self.__pill_color = ColorConstants.YELLOW
        self.__score = 0
        self.__matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2,
             2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2,
             2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0,
             0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0,
             0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0,
             0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0,
             0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2,
             2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2,
             2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2,
             2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2,
             1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def add_movable(self, movable):
        if type(movable) == PacMan.hero.Hero:
            self.hero = movable
        self.movables.append(movable)

    def remove_movable(self, movable):
        self.movables.remove(movable)

    def notify(self):
        for movable in self.movables:
            row = movable.row
            column = movable.column
            row_intention = movable.row_intention
            column_intention = movable.column_intention
            directions = self.get_directions(row, column)
            if len(directions) >= 3:
                movable.crossroad(directions)
            if isinstance(movable, PacMan.ghost.Ghost) and movable.row == self.hero.row\
                    and movable.column == self.hero.column:
                self.hero.lifes -= 1
                if self.hero.lifes <= 0:
                    self.game_state = GameStateConstants.GameOver
                else:
                    self.hero.row = 1
                    self.hero.column = 1
            else:
                if 0 <= column_intention < 28 and 0 <= row_intention < 29 \
                        and self.__matrix[int(row_intention)][int(column_intention)] != 2:
                    movable.accept_movement()
                    if isinstance(movable, PacMan.hero.Hero) and self.__matrix[row][column] == 1:
                        self.__score += 1
                        self.__matrix[row][column] = 0
                        if self.__score >= 306:
                            self.game_state = GameStateConstants.Victory
                else:
                    movable.refuse_movement(directions)

    def draw(self, game_screen):
        for line_index, line in enumerate(self.__matrix):
            self.draw_scenery_line(game_screen, line_index, line)
        self.draw_score(game_screen)
        if self.game_state == GameStateConstants.Paused:
            self.draw_state_message(game_screen, "P A U S E D")
        elif self.game_state == GameStateConstants.GameOver:
            self.draw_state_message(game_screen, "G A M E    O V E R")
        elif self.game_state == GameStateConstants.Victory:
            self.draw_state_message(game_screen, "Y O U    W O N ! ! !")

    def draw_state_message(self,game_screen, message):
        text_img = self.font.render(message, True, ColorConstants.YELLOW)
        text_x = (game_screen.get_width() - text_img.get_width()) // 2
        text_y = (game_screen.get_height() - text_img.get_height()) // 2
        game_screen.blit(text_img, (text_x, text_y))

    def event_processor(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.game_state == GameStateConstants.Paused:
                        self.game_state = GameStateConstants.Running
                    else:
                        self.game_state = GameStateConstants.Paused
            if e.type == pygame.QUIT:
                exit()

    def rules_calculator(self):
        if self.game_state == GameStateConstants.Paused:
            pass
        elif self.game_state == GameStateConstants.GameOver:
            pass
        elif self.game_state == GameStateConstants.Victory:
            pass
        else:
            self.notify()

    def draw_score(self, game_screen):  # Definindo fontes
        score_x = 30 * self.__column_size
        score_y = 50
        score_img = self.font.render("score: {} ".format(self.__score), True, self.__pill_color)
        game_screen.blit(score_img, (score_x, score_y))
        lifes = self.font.render("lifes: {} ".format(self.hero.lifes), True, self.__pill_color)
        game_screen.blit(lifes, (score_x, score_y + 50))

    def draw_scenery_line(self, game_screen, line_index, line):
        for column_index, column in enumerate(line):
            # coordenadas iniciais do retangulo e tamanho
            x = column_index * self.__column_size
            y = line_index * self.__column_size
            if column == 2:
                color = self.__tile_color
            else:
                color = self.__path_color
            pygame.draw.rect(game_screen, color,
                             (x, y, self.__column_size, self.__column_size), 0)
            if column == 1:
                x_center = x + self.__column_size // 2
                y_center = y + self.__column_size // 2
                pygame.draw.circle(game_screen, self.__pill_color, (
                    x_center, y_center), self.__column_size / 10, 0)

    def get_directions(self, row, column):
        directions = []
        if self.__matrix[int(row - 1)][int(column)] != 2:
            directions.append(MovementConstants.UP)
        if self.__matrix[int(row + 1)][int(column)] != 2:
            directions.append(MovementConstants.DOWN)
        if self.__matrix[int(row)][int(column - 1)] != 2:
            directions.append(MovementConstants.LEFT)
        if self.__matrix[int(row)][int(column + 1)] != 2:
            directions.append(MovementConstants.RIGHT)
        return directions

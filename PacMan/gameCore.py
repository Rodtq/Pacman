import pygame

from PacMan.colorConstants import ColorConstants
from PacMan.gameScreen import GameScreen
from PacMan.ghost import Ghost
from PacMan.hero import Hero
from PacMan.scenery import Scenery


class GameCore:
    def __init__(self):
        pygame.init()
        self.screenSettings = GameScreen()
        self.game_screen = pygame.display.set_mode((self.screenSettings.screen_width, self.screenSettings.screen_height), 0)
        character_size = self.screenSettings.screen_height // 30
        self.pacMan = Hero(character_size)
        self.ghost = Ghost(ColorConstants.RED, character_size)
        self.ghost1 = Ghost(ColorConstants.WHITE, character_size)
        self.ghost2 = Ghost(ColorConstants.BLUE, character_size)
        self.ghost3 = Ghost(ColorConstants.ORANGE, character_size)
        self.ghost4 = Ghost(ColorConstants.PINK, character_size)
        self.ghost5 = Ghost(ColorConstants.CYAN, character_size)
        self.stage = Scenery(self.screenSettings)
        self.stage.add_movable(self.pacMan)
        self.stage.add_movable(self.ghost)
        self.stage.add_movable(self.ghost1)
        self.stage.add_movable(self.ghost2)
        self.stage.add_movable(self.ghost3)
        self.stage.add_movable(self.ghost4)
        self.stage.add_movable(self.ghost5)

        self.run_game()

    def run_game(self):
        while True:
            self.pacMan.rules_calculator()
            self.ghost.rules_calculator()
            self.ghost1.rules_calculator()
            self.ghost2.rules_calculator()
            self.ghost3.rules_calculator()
            self.ghost4.rules_calculator()
            self.ghost5.rules_calculator()
            self.stage.rules_calculator()

            self.game_screen.fill(ColorConstants.BLACK)
            self.stage.draw(self.game_screen)
            self.pacMan.draw(self.game_screen)
            self.ghost.draw(self.game_screen)
            self.ghost1.draw(self.game_screen)
            self.ghost2.draw(self.game_screen)
            self.ghost3.draw(self.game_screen)
            self.ghost4.draw(self.game_screen)
            self.ghost5.draw(self.game_screen)

            pygame.display.update()
            pygame.time.delay(80)

            events = pygame.event.get()
            self.stage.event_processor(events)
            self.pacMan.event_processor(events)

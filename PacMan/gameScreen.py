from PacMan.gameElement import GameElement


class GameScreen(GameElement):
    def __init__(self):
        super().__init__()
        self.__screen_width = 800
        self.__screen_height = 600
        self.__column_size = self.__screen_height // 30

    def move(self):
        pass

    def draw(self, game_screen):
        pass

    def event_processor(self, events):
        pass

    def rules_calculator(self, events):
        pass

    @property
    def screen_width(self):
        return 800

    @property
    def screen_height(self):
        return self.__screen_height

    @property
    def column_size(self):
        return self.__column_size

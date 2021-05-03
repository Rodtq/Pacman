from abc import ABCMeta, abstractmethod


class GameElement(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, game_screen):
        raise NotImplementedError("An error occurred when drawing character")

    @abstractmethod
    def event_processor(self, events):
        raise NotImplementedError("An error occurred when drawing character")

    @abstractmethod
    def rules_calculator(self):
        raise NotImplementedError("An error occurred when drawing character")

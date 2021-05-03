from abc import ABCMeta


class MovableSubject(metaclass=ABCMeta):

    def add_movable(self, movable):
        pass

    def remove_movable(self, movable):
        pass

    def notify(self):
        pass

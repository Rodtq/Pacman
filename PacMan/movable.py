from abc import ABCMeta


class MovableObserver(metaclass=ABCMeta):

    def accept_movement(self):
        pass

    def refuse_movement(self, directions):
        pass

    def crossroad(self, directions):
        pass

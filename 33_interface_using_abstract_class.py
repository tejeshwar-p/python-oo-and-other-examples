from abc import ABC, abstractmethod

# There is no out of box support for interfaces in python so
# The below class is like an interface because
# all the methods in the class are abstract methods


class GamingConsole(ABC):

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass


class MarioGame(GamingConsole):
    def up(self):
        print("Up from MarioGame")

    def down(self):
        print("Down from MarioGame")

    def left(self):
        print("Left from MarioGame")

    def right(self):
        print("Right from MarioGame")


game = MarioGame()
game.up()
game.down()
game.left()
game.right()

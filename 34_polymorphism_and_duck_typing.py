from abc import ABC, abstractmethod


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


class ChessGame(GamingConsole):
    def up(self):
        print("Up from ChessGame")

    def down(self):
        print("Down from ChessGame")

    def left(self):
        print("Left from ChessGame")

    def right(self):
        print("Right from ChessGame")

# Below is an example of polymorphism


games = [MarioGame(), ChessGame()]

for game in games:
    game.up()
    game.down()
    game.left()
    game.right()

print("-----------------------------------------------------")

# Below two classes do not implement any interface


class LudoGame:
    def up(self):
        print("Up from LudoGame")

    def down(self):
        print("Down from LudoGame")

    def left(self):
        print("Left from LudoGame")

    def right(self):
        print("Right from LudoGame")


class SnakesAndLaddersGame:
    def up(self):
        print("Up from SnakesAndLaddersGame")

    def down(self):
        print("Down from SnakesAndLaddersGame")

    def left(self):
        print("Left from SnakesAndLaddersGame")

    def right(self):
        print("Right from SnakesAndLaddersGame")

# The below code still works even when there is no common class which
# the LudoGame and SnakesAndLaddersGame extend.
# This is called DUCK TYPING in python!


other_games = [LudoGame(), SnakesAndLaddersGame()]

for game in other_games:
    game.up()
    game.down()
    game.left()
    game.right()


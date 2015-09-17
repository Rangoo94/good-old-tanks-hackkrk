import random
from connections import Connection


class Game(object):
    def __init__(self):
        self.c = Connection()
        self.game = self.c.get_game()

    def start(self):
        print "-="*20
        print "GAME START"
        response = None
        while not response or not response.get('alive'):
            response = self.c.submit_move(
                move_distance=0,
                shot_angle=random.randrange(-90, 90),
                shot_power=random.randrange(1, 100)
            )
            print "-="*20
            print response


if __name__ == "__main__":
    game = Game()
    game.start()
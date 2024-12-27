from game.engine import Engine
from game.utils.generate_game import generate


if __name__ == '__main__':
    generate()
    engine = Engine(False)
    engine.loop()

    print('Everything is done!')

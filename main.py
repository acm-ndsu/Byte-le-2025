from game.engine import Engine
from game.utils.generate_game import generate


if __name__ == '__main__':
    for x in range(25):
        print(f'\n\n\n\n\nStarting game {x + 1}\n\n\n\n\n')
        generate()
        engine = Engine(False)
        engine.loop()

import os

import pygame
import pygame as pyg

from visualizer.bytesprites.bytesprite import ByteSprite
from game.utils.vector import Vector
from visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory


class CharactersBS(ByteSpriteFactory):

    @staticmethod
    def update(data: dict, layer: int, pos: Vector, spritesheets: list[list[pyg.Surface]]) -> list[pyg.Surface]:
        offset: int = 7 if data.get('country') == 2 else 0

        if data['state'] == 'attacking':
            return spritesheets[offset+1]
        if data['state'] == 'healing':
            return spritesheets[offset+2]
        if data['state'] == 'buffing':
            return spritesheets[offset+3]
        if data['state'] == 'debuffing':
            return spritesheets[offset+4]
        if data['state'] == 'attacked':
            return spritesheets[offset+5]
        if data['state'] == 'defeated':
            return spritesheets[offset+6]

        # If nothing else, idle sprite used at offset zero.
        return spritesheets[offset]


# Separate create bytesprite methods for each of the characters
    @staticmethod
    def create_anahita_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/anahitaSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_berry_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/berrySS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_calmus_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/calmusSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))\


    @staticmethod
    def create_fultra_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/fultraSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_irwin_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/irwinSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_ninlil_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/ninlilSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_gen_attacker_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/gen_attackerSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_gen_healer_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/gen_healerSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_tank_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/gen_tankSS.png'), 10, 4,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

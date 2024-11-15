import os

import pygame
import pygame as pyg

from visualizer.bytesprites.bytesprite import ByteSprite
from game.utils.vector import Vector
from visualizer.bytesprites.bytesprite_factory import ByteSpriteFactory


class CharactersBS(ByteSpriteFactory):

    @staticmethod
    def update(data: dict, layer: int, pos: Vector, spritesheets: list[list[pyg.Surface]]) -> list[pyg.Surface]:
        temp_spritesheet: list[pyg.Surface]

        if data['state'] == 'attacking':
            temp_spritesheet = spritesheets[1]
        elif data['state'] == 'healing':
            temp_spritesheet = spritesheets[2]
        elif data['state'] == 'buffing':
            temp_spritesheet = spritesheets[3]
        elif data['state'] == 'debuffing':
            temp_spritesheet = spritesheets[4]
        elif data['state'] == 'attacked':
            temp_spritesheet = spritesheets[5]
        elif data['state'] == 'defeated':
            temp_spritesheet = spritesheets[6]
        else:
            # If nothing else, idle sprite used at offset zero.
            temp_spritesheet = spritesheets[0]

        # If company is 1 (uroda), flip the sprites to face right
        if data.get('country') == 1:
            temp_spritesheet = [pygame.transform.flip(sprite, True, False) for sprite in temp_spritesheet]

        return temp_spritesheet


# Separate create bytesprite methods for each of the characters
    @staticmethod
    def create_anahita_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/anahita.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_berry_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/berry.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_calmus_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/calmus.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_fultra_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/fultra.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_irwin_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/irwin.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_ninlil_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/ninlil.png'), 7, 16,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_uroda_gen_attacker_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/uroda_gen_attacker.png'), 7, 12,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_uroda_gen_healer_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/uroda_gen_healer.png'), 7, 13,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_uroda_gen_tank_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/uroda_gen_tank.png'), 7, 14,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))
    
    @staticmethod
    def create_turpis_gen_attack_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/turpis_gen_attacker.png'), 7, 13,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))
    
    @staticmethod
    def create_turpis_gen_healer_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/turpis_gen_healer.png'), 7, 13,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))
    
    @staticmethod
    def create_turpis_gen_tank_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/turpis_gen_tank.png'), 7, 13,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

    @staticmethod
    def create_gen_trash_bytesprite(screen: pyg.Surface) -> ByteSprite:
        return ByteSprite(screen, os.path.join(os.getcwd(), 'visualizer/images/spritesheets/gen_trash.png'), 7, 13,
                          CharactersBS.update, colorkey=pygame.Color(255, 0, 255))

import pygame
import os

from game.utils.vector import Vector


class SpeedStat(pygame.sprite.Sprite):
    def __init__(self, top_left: Vector):
        super().__init__()
        self.images: dict[str | int, pygame.Surface] = {
            0: pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/speed_stat/speed_neutral.png')),
            1: pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/speed_stat/speed_buff.png')),
            2: pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/speed_stat/speed_debuff.png')),
        }

        self.image: pygame.Surface = self.images[0]
        self.character: str | int = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left.as_tuple()

    @property
    def character(self) -> str | int:
        return self.__character

    @character.setter
    def character(self, character: str | int) -> None:
        self.__character = character
        self.image = self.images[character]

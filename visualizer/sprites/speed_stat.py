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
        self.speed_stat: str | int = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left.as_tuple()

    @property
    def speed_stat(self) -> str | int:
        return self.__speed_stat

    @speed_stat.setter
    def speed_stat(self, speed_stat: str | int) -> None:
        self.__speed_stat = speed_stat
        self.image = self.images[speed_stat]

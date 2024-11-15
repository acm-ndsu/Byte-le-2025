import pygame
import os

from game.utils.vector import Vector


class Headshot(pygame.sprite.Sprite):
    def __init__(self, top_left: Vector):
        super().__init__()
        self.images: dict[str | int, pygame.Surface] = {
            'anahita': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/anahita_headshot.png')),
            'berry': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/berry_headshot.png')),
            'ninlil': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/ninlil_headshot.png')),
            'calmus': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/calmus_headshot.png')),
            'irwin': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/irwin_headshot.png')),
            'fultra': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/fultra_headshot.png')),
            'turpis_generic_attacker': pygame.image.load(os.path.join(os.getcwd(), 'visualizer/images/staticsprites/headshot/turpis_generic_attacker_headshot.png')),
            'turpis_generic_tank': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/turpis_generic_tank_headshot.png')),
            'turpis_generic_healer': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/turpis_generic_healer_headshot.png')),
            'uroda_generic_attacker': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/uroda_generic_attacker_headshot.png')),
            'uroda_generic_tank': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/uroda_generic_tank_headshot.png')),
            'uroda_generic_healer': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/uroda_generic_healer_headshot.png')),
            'generic_trash': pygame.image.load(os.path.join(os.getcwd(),'visualizer/images/staticsprites/headshot/generic_trash_headshot.png')),
        }

        self.image: pygame.Surface = self.images['generic_trash']
        self.character: str | int = 'generic_trash'
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left.as_tuple()

    @property
    def character(self) -> str | int:
        return self.__character

    @character.setter
    def character(self, character: str | int) -> None:
        self.__character = character
        self.image = self.images[character]

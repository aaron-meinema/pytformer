from abc import abstractmethod

import pygame


class Unit:
    def __init__(self, x: int, y: int, image_location: str):
        self.sheet = pygame.image.load(image_location).convert_alpha()
        self.rect = self.sheet.get_rect()

        self.frame_speed = 0.1

        self.rect.x = x
        self.rect.y = y

        self.frame_w = 24
        self.frame_h = 24

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    @abstractmethod
    def get_frame(self, index) -> pygame.Surface:
        pass

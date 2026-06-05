
import pygame

from src.creator.midground_types import UpperType
from src.creator.mouse_preview import MousePreview


class UnitSpawner:
    def __init__(self, creator):
        self.upper_type = UpperType.GRASS
        self.creator = creator
        self.mouse_tile = None
        self.mouse_preview = None
        self.clicked = False

    def on_loop(self) -> None:
        self.manage_keyboard()
        mouse_pos = pygame.mouse.get_pos()
        calculated_mouse_pos = (
            mouse_pos[0] - (mouse_pos[0] % 32) - 16,
            mouse_pos[1] - (mouse_pos[1] % 32) - 16)

        if pygame.mouse.get_pressed()[0] and not self.clicked:  # Left mouse button
            self.mouse_preview = MousePreview(
                self.upper_type,
                calculated_mouse_pos,
                self.creator)

            self.mouse_tile = None
            self.clicked = True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            if self.mouse_preview:
                new_units = self.mouse_preview.units(mouse_pos)
                self.creator.tiles.extend(new_units)
            self.mouse_preview = None

    def manage_keyboard(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            self.upper_type = UpperType.GRASS
        if keys[pygame.K_1]:
            self.upper_type = UpperType.DIRT
        if keys[pygame.K_2]:
            self.upper_type = UpperType.NONE
        if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
            self.creator.save()

    def on_render(self) -> None:
        if self.mouse_tile:
            self.creator._display_surf.blit(self.mouse_tile.image, self.mouse_tile.rect)
        if self.mouse_preview:
            self.mouse_preview.on_render()

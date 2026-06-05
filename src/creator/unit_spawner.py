
import pygame

from src.creator.mouse_preview import MousePreview
from src.field_tiles.tile import Tile


class UnitSpawner:
    def __init__(self, creator):
        self.selected_number = 0
        self.creator = creator
        self.mouse_tile = None
        self.mouse_preview = None
        self.clicked = False

    def on_loop(self) -> None:
        self.manage_keyboard()
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_tile = Tile(
            mouse_pos[0] -
            (mouse_pos[0] % 32) - 16,
            mouse_pos[1] -
            (mouse_pos[1] % 32) - 16,
            self.selected_number)
        calculated_mouse_pos = (
            mouse_pos[0] - (mouse_pos[0] % 32) - 16,
            mouse_pos[1] - (mouse_pos[1] % 32) - 16)

        if pygame.mouse.get_pressed()[0] and not self.clicked:  # Left mouse button
            self.mouse_preview = MousePreview(
                self.selected_number,
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
            self.selected_number = 0
        if keys[pygame.K_1]:
            self.selected_number = 1
        if keys[pygame.K_2]:
            self.selected_number = 2
        if keys[pygame.K_3]:
            self.selected_number = 3
        if keys[pygame.K_4]:
            self.selected_number = 4
        if keys[pygame.K_5]:
            self.selected_number = 5
        if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
            self.creator.save()

    def on_render(self) -> None:
        if self.mouse_tile:
            self.creator._display_surf.blit(self.mouse_tile.image, self.mouse_tile.rect)
        if self.mouse_preview:
            self.mouse_preview.on_render()

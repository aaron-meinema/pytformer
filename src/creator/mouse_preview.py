import pygame

from src.creator.midground_types import UpperType


class MousePreview:
    def __init__(self, upper_type: UpperType, mouse_begin_pos: tuple[int, int], creator):
        self.upper_type = upper_type
        self.mouse_begin_pos = mouse_begin_pos
        self.creator = creator

    def on_render(self) -> None:
        current_mouse = pygame.mouse.get_pos()
        rect = self._get_calculated_rect(current_mouse)
        self.creator._display_surf.fill(pygame.Color(0, 0, 200), rect)

    def units(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        return self._get_calculated_rect(current_mouse)

    def _get_calculated_rect(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        if True:
            return self._calculated_first_type(current_mouse)
        calculated_x = (current_mouse[0] - current_mouse[0] % 32) - self.mouse_begin_pos[0] - 16
        calculated_y = (current_mouse[1] - current_mouse[1] % 32) - self.mouse_begin_pos[1] - 16
        return pygame.Rect(
            self.mouse_begin_pos[0],
            self.mouse_begin_pos[1],
            calculated_x,
            calculated_y)

    def _calculated_first_type(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        calculated_x = (current_mouse[0] - current_mouse[0] % 32) - self.mouse_begin_pos[0] - 16
        if calculated_x < 0:
            offset = current_mouse[0] - current_mouse[0] % 32
            calculated_x = self.mouse_begin_pos[0] - offset + 16
            return pygame.Rect(
                offset,
                self.mouse_begin_pos[1],
                calculated_x,
                32)
        return pygame.Rect(
            self.mouse_begin_pos[0],
            self.mouse_begin_pos[1],
            calculated_x,
            32)

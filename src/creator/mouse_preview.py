import pygame

from src.field_tiles.tile import Tile


class MousePreview:
    def __init__(self, unit_number: int, mouse_begin_pos: tuple[int, int], creator):
        self.unit_number = unit_number
        self.mouse_begin_pos = mouse_begin_pos
        self.creator = creator

    def on_render(self) -> None:
        current_mouse = pygame.mouse.get_pos()
        rect = self._get_calculated_rect(current_mouse)
        self.creator._display_surf.fill(pygame.Color(0, 0, 200), rect)

    def units(self, current_mouse: tuple[int, int]) -> list[Tile]:
        rect = self._get_calculated_rect(current_mouse)
        return self._get_first_type(rect)

    def _get_calculated_rect(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        if self.unit_number == 0:
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


    @staticmethod
    def _get_first_type(rect: pygame.Rect) -> list[Tile]:
        units = []
        for x in range(rect.left, rect.right, 32):
            if x == rect.left:
                units.append(Tile(x, rect.top, 0))
            elif x == rect.right - 32:
                units.append(Tile(x, rect.top, 3))
            elif x % 64 == 16:  # noqa: PLR2004
                units.append(Tile(x, rect.top, 1))
            else:
                units.append(Tile(x, rect.top, 2))
        return units

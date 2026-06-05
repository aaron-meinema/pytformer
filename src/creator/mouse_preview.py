import pygame

from src.creator.midground_types import SizeType, UpperType


class MousePreview:
    def __init__(
            self,
            upper_type: UpperType,
            size_type: SizeType,
            mouse_begin_pos: tuple[int, int],
            creator):
        self.upper_type: UpperType = upper_type
        self.size_type: SizeType = size_type
        self.mouse_begin_pos: tuple[int, int] = mouse_begin_pos
        self.creator = creator

    def on_render(self) -> None:
        current_mouse = pygame.mouse.get_pos()
        rect = self._get_calculated_rect(current_mouse)
        self.creator._display_surf.fill(pygame.Color(0, 0, 200), rect)

    def units(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        return self._get_calculated_rect(current_mouse)

    def _get_calculated_rect(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        match self.size_type:
            case SizeType.SMALL:
                return self._calculated_small_type(current_mouse)
            case SizeType.MEDIUM:
                return self._calculated_medium_type(current_mouse)
            case SizeType.LARGE:
                return self._calculated_small_type(current_mouse)
        # calculated_x = (current_mouse[0] - current_mouse[0] % 32) - self.mouse_begin_pos[0] - 16
        # calculated_y = (current_mouse[1] - current_mouse[1] % 32) - self.mouse_begin_pos[1] - 16
        # return pygame.Rect(
        #    self.mouse_begin_pos[0],
        #    self.mouse_begin_pos[1],
        #    calculated_x,
        #    calculated_y)

    def _calculated_small_type(self, current_mouse: tuple[int, int]) -> pygame.Rect:
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

    def _calculated_medium_type(self, current_mouse: tuple[int, int]) -> pygame.Rect:
        calculated_x = (current_mouse[0] - current_mouse[0] % 32) - self.mouse_begin_pos[0] - 16
        if calculated_x < 0:
            offset = current_mouse[0] - current_mouse[0] % 32
            calculated_x = self.mouse_begin_pos[0] - offset + 16
            return pygame.Rect(
                offset,
                self.mouse_begin_pos[1],
                calculated_x,
                64)
        return pygame.Rect(
            self.mouse_begin_pos[0],
            self.mouse_begin_pos[1],
            calculated_x,
            64)

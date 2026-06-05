import pygame

from src.creator.midground_types import RowType, SizeType, UpperType
from src.creator.mouse_preview import MousePreview
from src.field_tiles.tile import Tile


class UnitSpawner:
    def __init__(self, creator):
        self.upper_type = UpperType.GRASS
        self.size_type = SizeType.SMALL
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
                self.size_type,
                calculated_mouse_pos,
                self.creator)

            self.mouse_tile = None
            self.clicked = True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            if self.mouse_preview:
                positions = self.mouse_preview.units(mouse_pos)
                new_units = self.get_units(positions)
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
        if keys[pygame.K_s]:
            self.size_type = SizeType.SMALL
        if keys[pygame.K_m]:
            self.size_type = SizeType.MEDIUM
        if keys[pygame.K_l]:
            self.size_type = SizeType.LARGE
        if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
            self.creator.save()

    def on_render(self) -> None:
        if self.mouse_tile:
            self.creator._display_surf.blit(self.mouse_tile.image, self.mouse_tile.rect)
        if self.mouse_preview:
            self.mouse_preview.on_render()

    def get_units(self, rect: pygame.Rect) -> list[Tile]:
        match (self.size_type):
            case SizeType.SMALL:
                return self._get_small_type(rect)
            case SizeType.MEDIUM:
                return self._get_medium_type(rect)
            case SizeType.LARGE:
                return self._get_small_type(rect)

    def _get_small_type(self, rect: pygame.Rect) -> list[Tile]:
        units = []
        offset = self._get_offset_upper_type()
        for x in range(rect.left, rect.right, 32):
            if x == rect.left and x == (rect.right - 32):
                units.append(Tile(x, rect.top, RowType.SINGLE, 24))
            elif x == rect.left:
                units.append(Tile(x, rect.top, RowType.SINGLE, offset + 0))
            elif x == rect.right - 32:
                units.append(Tile(x, rect.top, RowType.SINGLE, offset + 3))
            elif x % 64 == 16:  # noqa: PLR2004
                units.append(Tile(x, rect.top, RowType.SINGLE, offset + 1))
            else:
                units.append(Tile(x, rect.top, RowType.SINGLE, offset + 2))
        return units

    def _get_medium_type(self, rect: pygame.Rect) -> list[Tile]:
        return self._get_small_type(rect)
        units = []
        offset = self._get_offset_upper_type()
        for x in range(rect.left, rect.right, 32):
            for y in range(rect.top, rect.bottom, 32):
                xy_rect: tuple[int, int] = (x, y)
                # if xy_rect == rect.topleft:

    def _get_offset_upper_type(self) -> int:
        match (self.upper_type):
            case UpperType.GRASS:
                return 0
            case UpperType.DIRT:
                return 6
            case UpperType.NONE:
                return 18

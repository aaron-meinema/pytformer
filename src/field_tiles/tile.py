from __future__ import annotations

import pygame

from src.creator.midground_types import RowType


class Tile:
    def __init__(self, x: int, y: int, row_type: RowType, image_number: int):
        self.full_image = pygame.image.load(
            "assets/sprites/tiles/midground_/summer_.png").convert_alpha()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        # row_offset = self._get_row_offset()
        self.image.blit(self.full_image, (0, 0), (image_number * 8, 8, 8, 8))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.overlap_threshold = 20
        self.image_number = image_number
        self.row_type = row_type

    def get_width(self) -> int:
        return self.rect.width

    def get_height(self) -> int:
        return self.rect.height

    def get_position(self) -> tuple:
        return self.rect.topleft

    def on_floor(self, unit_rect: pygame.Rect) -> bool:
        if not self.rect.colliderect(unit_rect):
            return False

        overlap = (
            min(unit_rect.right, self.rect.right) -
            max(unit_rect.left, self.rect.left) -
            self.overlap_threshold
        )
        if overlap <= 0:
            return False
        return (unit_rect.bottom - 8) <= self.rect.top

    def on_wall(self, unit_rect: pygame.Rect) -> bool:
        return self.rect.colliderect(unit_rect) and (unit_rect.right >= self.rect.left - 10 and
                                                     unit_rect.left <= self.rect.right + 10)

    def to_json(self) -> dict:
        return {
            "x": self.rect.x,
            "y": self.rect.y,
            "row_type": self.row_type.get_value(),
            "image_number": self.image_number
        }

    def _get_row_offset(self) -> int:
        match self.row_type:
            case RowType.SINGLE:
                return 0
            case RowType.DUAL_TOP:
                return 3
            case RowType.DUAL_BOTTOM:
                return 4

    @classmethod
    def from_json(cls, data: dict) -> Tile:
        return cls(data["x"], data["y"], RowType.from_value(data["row_type"]), data["image_number"])

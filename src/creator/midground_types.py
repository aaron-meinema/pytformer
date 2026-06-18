from __future__ import annotations

from enum import Enum


class UpperType(Enum):
    GRASS = 0,
    DIRT = 1,
    NONE = 2


class GroundType(Enum):
    BROWN = 0,
    DARK_GREY = 1,
    LIGHT_GREY = 2,


class SizeType(Enum):
    SMALL = 0,
    MEDIUM = 1,
    LARGE = 2


class SeasonType(Enum):
    SUMMER = 0,
    WINTER = 1,


class RowType(Enum):
    SINGLE = 0,
    DUAL_TOP = 1,
    DUAL_BOTTOM = 2

    def get_value(self) -> int:
        match self:
            case self.SINGLE:
                return 0
            case self.DUAL_TOP:
                return 1
            case self.DUAL_BOTTOM:
                return 2

    @staticmethod
    def from_value(number: int) -> RowType:
        if number == 0:
            return RowType.SINGLE
        elif number == 1:
            return RowType.DUAL_TOP
        else:
            return RowType.DUAL_BOTTOM

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

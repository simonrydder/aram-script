from enum import StrEnum


class DataColumn(StrEnum):
    NAME = "name"
    RELEASE_DATE = "release-date"
    IMG_FULL_SRC = "image-full-src"
    DMG = "damage"
    TOUGHNESS = "toughness"
    CONTROL = "control"
    MOBILITY = "mobility"
    UTILITY = "utility"

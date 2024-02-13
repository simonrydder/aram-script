from enum import IntEnum
from typing import Literal


class RatingScale(IntEnum):
    ONE = 1
    TWO = 2
    TREE = 3


LiteralRatingScale = Literal[1, 2, 3]

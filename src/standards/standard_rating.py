from src.enums.rating_scale import LiteralRatingScale, RatingScale
from src.interfaces.rating import Rating


class StandardRating(Rating):
    def __init__(
        self,
        damage: RatingScale | LiteralRatingScale,
        toughness: RatingScale | LiteralRatingScale,
        control: RatingScale | LiteralRatingScale,
        mobility: RatingScale | LiteralRatingScale,
        utility: RatingScale | LiteralRatingScale,
    ) -> None:
        super().__init__(damage, toughness, control, mobility, utility)
        self._total: int = self._sum_ratings()

    def _get_rating_scale(self, value: RatingScale | LiteralRatingScale) -> RatingScale:
        if isinstance(value, RatingScale):
            return value

        return RatingScale(value)

    @property
    def damage(self) -> RatingScale:
        return self._damage

    @damage.setter
    def damage(self, value: RatingScale) -> None:
        self._damage = value

    @property
    def toughness(self) -> RatingScale:
        return self._toughness

    @toughness.setter
    def toughness(self, value: RatingScale) -> None:
        self._toughness = value

    @property
    def control(self) -> RatingScale:
        return self._control

    @control.setter
    def control(self, value: RatingScale) -> None:
        self._control = value

    @property
    def mobility(self) -> RatingScale:
        return self._mobility

    @mobility.setter
    def mobility(self, value: RatingScale) -> None:
        self._mobility = value

    @property
    def utility(self) -> RatingScale:
        return self._utility

    @utility.setter
    def utility(self, value: RatingScale) -> None:
        self._utility = value

    @property
    def total(self) -> int:
        return self._total

    @total.setter
    def total(self, value: int) -> None:
        self._total = value

    def _sum_ratings(self) -> int:
        return (
            self.damage + self.toughness + self.control + self.mobility + self.utility
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rating):
            return False

        if not self._has_equal_damage(other):
            return False

        if not self._has_equal_thoughness(other):
            return False

        if not self._has_equal_control(other):
            return False

        if not self._has_equal_mobility(other):
            return False

        if not self._has_equal_utility(other):
            return False

        return True

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Rating):
            raise TypeError(f"Object {other} is not of type {type(Rating)}")

        return self.total < other.total

    def _has_equal_utility(self, other: Rating) -> bool:
        return self.utility == other.utility

    def _has_equal_mobility(self, other: Rating) -> bool:
        return self.mobility == other.mobility

    def _has_equal_control(self, other: Rating) -> bool:
        return self.control == other.control

    def _has_equal_thoughness(self, other: Rating) -> bool:
        return self.toughness == other.toughness

    def _has_equal_damage(self, other: Rating) -> bool:
        return self.damage == other.damage

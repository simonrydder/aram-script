from abc import ABC, abstractmethod

from src.enums.rating_scale import LiteralRatingScale, RatingScale


class Rating(ABC):
    def __init__(
        self,
        damage: RatingScale | LiteralRatingScale,
        toughness: RatingScale | LiteralRatingScale,
        control: RatingScale | LiteralRatingScale,
        mobility: RatingScale | LiteralRatingScale,
        utility: RatingScale | LiteralRatingScale,
    ) -> None:
        super().__init__()
        self._damage = self._get_rating_scale(damage)
        self._toughness = self._get_rating_scale(toughness)
        self._control = self._get_rating_scale(control)
        self._mobility = self._get_rating_scale(mobility)
        self._utility = self._get_rating_scale(utility)
        self._total: int = 0

    @abstractmethod
    def _get_rating_scale(self, value: RatingScale | LiteralRatingScale) -> RatingScale:
        pass

    @property
    @abstractmethod
    def damage(self) -> RatingScale:
        pass

    @damage.setter
    @abstractmethod
    def damage(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def toughness(self) -> RatingScale:
        pass

    @toughness.setter
    @abstractmethod
    def toughness(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def control(self) -> RatingScale:
        pass

    @control.setter
    @abstractmethod
    def control(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def mobility(self) -> RatingScale:
        pass

    @mobility.setter
    @abstractmethod
    def mobility(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def utility(self) -> RatingScale:
        pass

    @utility.setter
    @abstractmethod
    def utility(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def total(self) -> int:
        pass

    @total.setter
    @abstractmethod
    def total(self, value: int) -> None:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        pass

from abc import ABC, abstractmethod

from src.enums.rating_scale import RatingScale


class Rating(ABC):
    def __init__(
        self,
        damage: RatingScale,
        toughness: RatingScale,
        control: RatingScale,
        mobility: RatingScale,
        utility: RatingScale,
    ) -> None:
        super().__init__()
        self._damage = damage
        self._toughness = toughness
        self._control = control
        self._mobility = mobility
        self._utility = utility
        self._total: int = 0

    @property
    @abstractmethod
    def damage(self) -> RatingScale:
        return RatingScale.ONE

    @damage.setter
    @abstractmethod
    def damage(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def toughness(self) -> RatingScale:
        return RatingScale.ONE

    @toughness.setter
    @abstractmethod
    def toughness(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def control(self) -> RatingScale:
        return RatingScale.ONE

    @control.setter
    @abstractmethod
    def control(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def mobility(self) -> RatingScale:
        return RatingScale.ONE

    @mobility.setter
    @abstractmethod
    def mobility(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def utility(self) -> RatingScale:
        return RatingScale.ONE

    @utility.setter
    @abstractmethod
    def utility(self, value: RatingScale) -> None:
        pass

    @property
    @abstractmethod
    def total(self) -> int:
        return 0

    @total.setter
    @abstractmethod
    def total(self, value: int) -> None:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        return False

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        return False

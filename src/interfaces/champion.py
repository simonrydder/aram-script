from abc import ABC, abstractmethod
from datetime import date

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.rating import Rating


class Champion(ABC):
    def __init__(
        self,
        name: str,
        release_date: date,
        range_type: RangeType,
        damage_type: DamageType,
        resource: ResourceType,
        rating: Rating,
    ) -> None:
        super().__init__()
        self._name = name
        self._release_date = release_date
        self._range_type = range_type
        self._damage_type = damage_type
        self._resource = resource
        self._rating = rating

    # stats: Stats
    # champ_class: ChampionClass
    # champ_legacy: ChampionLegacy
    # image: ChampionImage

    @property
    @abstractmethod
    def rating(self) -> Rating:
        pass

    @rating.setter
    @abstractmethod
    def rating(self, value: Rating) -> None:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def release_date(self) -> date:
        pass

    @release_date.setter
    @abstractmethod
    def release_date(self, value: date) -> None:
        pass

    @property
    @abstractmethod
    def range_type(self) -> RangeType:
        pass

    @range_type.setter
    @abstractmethod
    def range_type(self, value: RangeType) -> None:
        pass

    @property
    @abstractmethod
    def damage_type(self) -> DamageType:
        pass

    @damage_type.setter
    @abstractmethod
    def damage_type(self, value: DamageType) -> None:
        pass

    @property
    @abstractmethod
    def resource(self) -> ResourceType:
        pass

    @resource.setter
    @abstractmethod
    def resource(self, value: ResourceType) -> None:
        pass

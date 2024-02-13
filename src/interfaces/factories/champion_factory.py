from abc import ABC, abstractmethod
from datetime import date

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.rating import Rating


class ChampionFactory(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_release_date(self) -> date:
        pass

    @abstractmethod
    def get_range_type(self) -> RangeType:
        pass

    @abstractmethod
    def get_damage_type(self) -> DamageType:
        pass

    @abstractmethod
    def get_resource(self) -> ResourceType:
        pass

    @abstractmethod
    def get_rating(self) -> Rating:
        pass

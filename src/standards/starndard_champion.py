from datetime import date

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.champion import Champion
from src.interfaces.rating import Rating


class StandardChampion(Champion):
    def __init__(
        self,
        name: str,
        release_date: date,
        range_type: RangeType,
        damage_type: DamageType,
        resource: ResourceType,
        rating: Rating,
    ) -> None:
        super().__init__(name, release_date, range_type, damage_type, resource, rating)

    @property
    def rating(self) -> Rating:
        return self._rating

    @rating.setter
    def rating(self, value: Rating) -> None:
        raise ValueError("Rating has already been set")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        raise ValueError("Name has already been set")

    @property
    def release_date(self) -> date:
        return self._release_date

    @release_date.setter
    def release_date(self, value: date) -> None:
        raise ValueError("Release Date has already been set")

    @property
    def range_type(self) -> RangeType:
        return self._range_type

    @range_type.setter
    def range_type(self, value: RangeType) -> None:
        raise ValueError("RangeType has already been set")

    @property
    def damage_type(self) -> DamageType:
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value: DamageType) -> None:
        raise ValueError("DamageType has already been set")

    @property
    def resource(self) -> ResourceType:
        return self._resource

    @resource.setter
    def resource(self, value: ResourceType) -> None:
        raise ValueError("Resource has already been set")

from codecs import raw_unicode_escape_decode
from datetime import date
from multiprocessing import Value

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.champion import Champion


class StandardChampion(Champion):
    def __init__(
        self,
        name: str,
        release_date: date,
        range_type: RangeType,
        damage_type: DamageType,
        resource: ResourceType,
    ) -> None:
        super().__init__(name, release_date, range_type, damage_type, resource)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if self._name != "":
            raise ValueError("Name has already been set")

        self._name = value

    @property
    def release_date(self) -> date:
        return self._release_date

    @release_date.setter
    def release_date(self, value: date) -> None:
        if self._release_date != date(0, 0, 0):
            raise ValueError("Release Date has already been set")

        self._release_date = value

    @property
    def range_type(self) -> RangeType:
        return self._range_type

    @range_type.setter
    def range_type(self, value: RangeType) -> None:
        if self._range_type != RangeType.NONE:
            raise ValueError("RangeType has already been set")

        self._range_type = value

    @property
    def damage_type(self) -> DamageType:
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value: DamageType) -> None:
        if self._damage_type != DamageType.NONE:
            raise ValueError("DamageType has already been set")

        self._damage_type = value

    @property
    def resource(self) -> ResourceType:
        return self._resource

    @resource.setter
    def resource(self, value: ResourceType) -> None:
        if self._resource != ResourceType.NONE:
            raise ValueError("Resource has already been set")

        self._resource = ResourceType.HEALTH

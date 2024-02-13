from datetime import date

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.factories.champion_factory import ChampionFactory
from src.interfaces.rating import Rating
from src.standards.standard_rating import StandardRating


class TestBChampionFactory(ChampionFactory):
    def get_name(self) -> str:
        return "Ahri"

    def get_damage_type(self) -> DamageType:
        return DamageType.MAGIC

    def get_range_type(self) -> RangeType:
        return RangeType.RANGED

    def get_rating(self) -> Rating:
        return StandardRating(2, 1, 2, 1, 1)

    def get_release_date(self) -> date:
        return date(2020, 5, 19)

    def get_resource(self) -> ResourceType:
        return ResourceType.MANA

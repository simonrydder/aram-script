from datetime import date

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.interfaces.factories.champion_factory import ChampionFactory
from src.interfaces.rating import Rating
from src.standards.standard_rating import StandardRating


class TestAChampionFactory(ChampionFactory):
    def get_name(self) -> str:
        return "Aatrox"

    def get_damage_type(self) -> DamageType:
        return DamageType.PHYSICAL

    def get_range_type(self) -> RangeType:
        return RangeType.MEELE

    def get_rating(self) -> Rating:
        return StandardRating(1, 2, 3, 3, 3)

    def get_release_date(self) -> date:
        return date(2023, 6, 13)

    def get_resource(self) -> ResourceType:
        return ResourceType.MANALESS

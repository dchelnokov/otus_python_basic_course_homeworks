"""
Create class `Plane`, that inherits from `Vehicle`
"""

from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


@dataclass()
class Plane(Vehicle):
    cargo: int = 0  # kg, current cargo weight
    max_cargo: int = 3000  # kg, maximal cargo weight

    def __init__(self, *kwargs):
        super().__init__()
    def load_cargo(self, added_load: int) :
        """
        method loads the plane with more cargo and updates the internal
        property cargo
        :param added_load: float is the amount of kilograms to be loaded
        :return:
        """
        if self.cargo + added_load <= self.max_cargo:
            self.cargo += added_load
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> int:
        """
        method returns the value of cargo and resets the cargo counter
        :return: float - the amount of unloaded cargo
        """
        result = self.cargo
        self.cargo = 0
        return result

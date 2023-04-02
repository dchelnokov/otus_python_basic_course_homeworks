"""
Create class `Plane`, that inherits from `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self,
                 weight: int,
                 fuel: int,
                 fuel_consumption: int,
                 max_cargo:int):
        super().__init__()
        self.cargo = 0
        self.max_cargo = max_cargo
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.weight = weight

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
        :return: ints - the amount of unloaded cargo
        """

        result = self.cargo
        self.cargo = 0
        return result

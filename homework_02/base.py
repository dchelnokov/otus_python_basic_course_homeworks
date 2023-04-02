from abc import ABC
from dataclasses import dataclass

from homework_02.exceptions import LowFuelError, NotEnoughFuel


@dataclass
class Vehicle(ABC):
    weight: int
    started: bool
    fuel: int  # liters
    fuel_consumption: int = 8  # liters per 100 km

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.weight = kwargs.get('weight', 0)
        self.fuel = kwargs.get('fuel', 40)
        self.fuel_consumption = kwargs.get('fuel_consumption', 2)
        self.started = False
        if not self.fuel:
            self.fuel = 0
    def start(self):
        if not self.started:
            if self.fuel < self.fuel_consumption :
                raise LowFuelError
            else:
                self.started = True

    def move(self, distance: int):
        """
        :param self: parent object
        :param distance: int - distance in km
        :return: void
        this method checks the fuel sufficiency to move the vehicle to
        the given distance.
        The fuel level will be changed according to the vehicle consumption
        by insufficient fuel level raises NotEnoughFuel
        """

        required_fuel = distance * (self.fuel_consumption )
        fuel_now = self.fuel
        if fuel_now < required_fuel or fuel_now < self.fuel_consumption:
            raise NotEnoughFuel
        else:
            self.fuel -=  required_fuel

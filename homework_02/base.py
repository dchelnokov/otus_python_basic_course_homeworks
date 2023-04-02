from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel



class Vehicle(ABC):

    def __init__(self, weight=0, fuel = 40,  fuel_consumption= 5 ):
        super().__init__()
        self.weight = weight
        self.fuel =     fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
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

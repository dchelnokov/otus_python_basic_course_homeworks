"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self):
        super().__init__()
class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__()

class CargoOverload(Exception):
    def __init__(self):
        super().__init__()

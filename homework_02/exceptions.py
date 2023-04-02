"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self):
        super().__init__(*args, **kwargs)
class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__(*args, **kwargs)

class CargoOverload(Exception):
    def __init__(self):
        super().__init__(*args, **kwargs)

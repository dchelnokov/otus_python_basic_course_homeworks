from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.engine import Engine
@dataclass()
class Car(Vehicle):
    engine: Engine = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = Engine(volume=3.2, pistons=6)

    def set_engine(self, engine: Engine):
        """
        set_engine sets the Engine::engine to the current instance
        of the class Car
        :param engine: Engine
        :return: void
        """
        if isinstance(engine, Engine):
            self.engine = engine
from sqlalchemy import (Column, Integer)
from sqlalchemy.orm import (DeclarativeBase, declared_attr)

class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

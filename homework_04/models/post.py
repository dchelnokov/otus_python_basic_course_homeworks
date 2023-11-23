# for the model Post the following fields are required:
# - user_id,
# - title,
# - body
# Create relationship with User

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship
from homework_04.base_model import Base


class Post(Base):

    title = Column(String(120), nullable=False, unique=False)
    body = Column(Text(), nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(
        "User",
        back_populates="post",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.user_id!r}"
        )
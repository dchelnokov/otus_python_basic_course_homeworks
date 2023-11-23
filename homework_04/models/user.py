from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from homework_04.base_model import Base

# Obligatory fields for the User model are:
#   name
#   username
#   email
# Create relationship with post

class User(Base):

    username = Column(String(80), nullable=False, unique=True)
    name = Column(String(50), nullable= False, unique=False)
    email = Column(String(120), nullable=False, unique=True)

    posts = relationship(
        "Post",
        back_populates="user",
        userlist=True
    )
    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username}, email={self.email}"
        )


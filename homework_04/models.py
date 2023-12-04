"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:

"""

import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey

from homework_04.config import DB_URL, DB_ECHO

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or DB_URL or "postgresql+asyncpg://postgres:password@localhost/postgres"
)


async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Session = async_session


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


# Obligatory fields for the User model are:
#   name
#   username
#   email
# Create relationship with post


class User(Base):
    username = Column(String(80), nullable=False, unique=True)
    name = Column(String(50), nullable=False, unique=False)
    email = Column(String(120), nullable=False, unique=True)

    posts = relationship("Post", back_populates="users", uselist=True)
    post = relationship("Post", back_populates="users", uselist=False)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username}, email={self.email}"
        )


class Post(Base):
    title = Column(String(120), nullable=False, unique=False)
    body = Column(Text(), nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.user_id!r}"
        )

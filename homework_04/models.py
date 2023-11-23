"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:


"""

import os
from sqlalchemy.ext.asyncio import AsyncSession
from base_model import Base
from models.user import User
from models.post import Post

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

Base = Base
Session = AsyncSession(...)


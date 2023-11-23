"""
Home work №4
Asynchronous work with the Network and DB

Extend the main, to execute the full program cycle
(add the async_main invokation):
- creating tables (initialisation)
- load users and posts
    - the post and users data should be loaded simultaneously
      with asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- add users and posts into the data base
  (using the data obtained from request relay them to a function to save in the DB)
- terminate theconnection to the DB
"""

import alembic.config
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from homework_04.config import DB_URL, DB_ECHO

async_engine = create_async_engine(
    url=DB_URL,
    echo=DB_ECHO,
)
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db() -> bool:
    """
    runs alembic update head to make sure that schema is configured
    returns: bool True if no exception was thrown, else False
    """
    alembicArgs = [
        'upgrade',
        'head',
    ]
    try:
        await alembic.config.main(alembicArgs)
    except Exception as e:
        print(f"Failed to init the Database with alembic. Error:{e}")
        return False
    return True


async def async_main():
    with async_session(async_engine) as session:
        pass


def main():
    asyncio.run(init_db())   # Prepare the DB Scheme before beginning
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

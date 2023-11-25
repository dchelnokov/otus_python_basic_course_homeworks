"""
Home work №4
Asynchronous work with the Network and DB

Extend the main, to execute the full program cycle
(add the async_main invocation):
- creating tables (initialization)
- load users and posts
    - the post and users data should be loaded simultaneously
      with asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- add users and posts into the DB
  (using the data obtained from request relay them to a function to save in the DB)
- terminate the connection to the DB
"""

import alembic.config
import asyncio

from models import async_engine, async_session


def init_db() -> bool:
    """
    runs alembic update head to make sure that schema is configured
    returns: bool True if no exception was thrown, else False
    """
    alembicArgs = [
        'upgrade',
        'head',
    ]
    try:
        alembic.config.main(alembicArgs)
    except Exception as e:
        print(f"Failed to init the Database with alembic. Error:{e}")
        return False

    return True


async def async_main():
    with async_session() as session:
        pass


def main():
    init_db()   # Prepare the DB Scheme before beginning
   # asyncio.run(async_main())


if __name__ == "__main__":
    main()

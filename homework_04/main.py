"""
Homework №4
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
import asyncio

import alembic.config
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from models import async_session, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def add_user(session: AsyncSession, user_data: dict) -> User:
    """
    creates a user with data from user_data to db
    """
    name = user_data.get("name", "Unknown")
    username = user_data.get("username", "No Data")
    email = user_data.get("email", "No Data")
    print(f"trying to create a user {name!r} with username {username!r}")
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def add_post(session: AsyncSession, post_data: dict) -> Post:
    """
    creates a post record with data from post_data to the DB
    """
    title = post_data.get("title", "No Data")
    body = post_data.get("body", "No Data")
    user_id = post_data.get("userId", 0)

    post = Post(title=title, body=body, user_id=user_id)
    session.add(post)
    await session.commit()

    return post


def init_db() -> bool:
    """
    runs alembic update head to make sure that schema is configured
    returns: bool True if no exception was thrown, else False
    """
    alembic_args = [
        "upgrade",
        "head",
    ]
    try:
        alembic.config.main(alembic_args)
    except Exception as e:
        print(f"Failed to init the Database with alembic. Error:{e}")
        return False

    return True


async def async_main():

    async with async_session() as session:

        async with asyncio.TaskGroup() as tg:
            users_task = tg.create_task(fetch_users_data(), name="getting_users")
            posts_task = tg.create_task(fetch_posts_data(), name="getting_posts")

        for user_dict in users_task.result():
            user_record = await add_user(session, user_dict)
            print(f"added user {user_record}")

        for post_dict in posts_task.result():
            await add_post(session, post_dict)
    print("Connection to the database is closed by leaving the context manager.")


def main():
    init_db()  # Prepare the DB Scheme before beginning
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

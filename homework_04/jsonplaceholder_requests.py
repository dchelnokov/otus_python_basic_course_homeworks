"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

from aiohttp import ClientSession


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


# {userId: int, id: int, title: str, body: str}
async def fetch_data(url: str) -> dict:
    async with ClientSession() as Session:
        async with Session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data() -> dict:
    return await fetch_data(USERS_DATA_URL)


async def fetch_posts_data() -> dict:
    return await fetch_data(POSTS_DATA_URL)


async def main():
    async with asyncio.TaskGroup() as tg:
        task_users = tg.create_task(fetch_users_data(), name="get-user-data")
        task_posts = tg.create_task(fetch_posts_data(), name="get-posts-data")

    print("    Users:\n", task_users.result())
    print("\n    Posts:\n", task_posts.result())


if __name__ == "__main__":
    asyncio.run(main())

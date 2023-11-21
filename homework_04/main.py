"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import alembic.config
import asyncio
def init_db() -> bool:
    """
    runs alembic update head to make sure that schema is configured
    returns: bool True if no exception was thrown, else False
    """
    alembicArgs = [
        '--rauseerr',
        'upgrade',
        'head',
    ]
    try:
        alembic.config.main(alembicArgs)
    except e:
        print(f"Failed to init the Database with alembic. Error:{e}")
        return False
    return True


async def async_main():
    pass


def main():
    init_db()   # Prepare the DB Scheme before beginning
    asyncio.run(async_main())



if __name__ == "__main__":
    main()

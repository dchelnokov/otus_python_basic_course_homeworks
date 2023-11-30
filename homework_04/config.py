from pathlib import Path

BASE_DIR = Path(__file__).parent
# db_file_path = BASE_DIR / "blog.db"

DB_URL = "postgresql+asyncpg://user:example@localhost:5432/homework_4"
DB_ECHO = False



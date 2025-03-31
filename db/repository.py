from typing import List, Tuple
import aiosqlite

from config import DB_PATH


class Repository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def initialize(self):
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                """CREATE TABLE IF NOT EXISTS parse_sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            url VARCHAR(255),
            xpath VARCHAR(255));
            """
            )

    async def add_data(self, data: List[Tuple]):
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.executemany(
                "INSERT INTO parse_sources (title, url, xpath) VALUES (?, ?, ?)", data
            )
            await conn.commit()


repo = Repository(DB_PATH)

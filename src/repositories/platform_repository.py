import sqlite3
from typing import Dict, Any, Tuple

class PlatformRepository:

  @staticmethod
  def insertPlatform(platform_data: Dict[str, Any]) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO platforms(name) VALUES (?)", (platform_data['name'],))

      con.commit()
  
  @staticmethod
  def getPlatformByName(name: str) -> Tuple[str, str]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      return cur.execute("SELECT id, name FROM platforms WHERE name = ?", (name,)).fetchone()
  
  @staticmethod
  def getPlatformByID(platform_id: int) -> Tuple[Any]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      platform_data = cur.execute("SELECT id, name FROM platforms WHERE id = ?", (platform_id,)).fetchone()

      return platform_data
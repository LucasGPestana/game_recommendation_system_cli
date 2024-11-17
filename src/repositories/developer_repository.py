import sqlite3
from typing import Dict, Any, Tuple

class DeveloperRepository:

  @staticmethod
  def insertDeveloper(developer_data: Dict[str, Any]) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO developers(name) VALUES (?)", (developer_data['name'],))

      con.commit()
  
  @staticmethod
  def getDeveloperByName(name: str) -> Tuple[str, str]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      return cur.execute("SELECT id, name FROM developers WHERE name = ?", (name,)).fetchone()
  
  @staticmethod
  def getDeveloperByID(developer_id: int) -> Tuple[Any]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      developer_data = cur.execute("SELECT id, name FROM developers WHERE id = ?", (developer_id,)).fetchone()

      return developer_data
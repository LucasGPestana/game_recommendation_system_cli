import sqlite3
from typing import Dict, Any, Tuple

class GenreRepository:

  @staticmethod
  def insertGenre(genre_data: Dict[str, Any]) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO genres(name) VALUES (?)", (genre_data["name"],))

      con.commit()
  
  @staticmethod
  def getGenreByName(name: str) -> Tuple[Any]:

    print(name)

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      return cur.execute("SELECT id, name FROM genres WHERE name = ?", (name,)).fetchone()
  
  @staticmethod
  def getGenreByID(genre_id: str) -> Tuple[Any]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      genre_data = cur.execute("SELECT id, name FROM genres WHERE id = ?", (genre_id,)).fetchone()

      return genre_data


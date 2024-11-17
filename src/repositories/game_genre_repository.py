import sqlite3

from typing import List

class GameGenreRepository:

  @staticmethod
  def insertGameGenreRelation(game_id: int, genre_id: int) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO games_genres(game_id, genre_id) VALUES (?, ?)", (game_id, genre_id))

      con.commit()
  
  @staticmethod
  def getGenresIDsByGameID(game_id) -> List[int]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      genres_ids = cur.execute(f"SELECT genre_id FROM games_genres WHERE game_id = ?", (game_id,)).fetchall()

      return list(map(lambda x: x[0], genres_ids))
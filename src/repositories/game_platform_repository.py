import sqlite3

from typing import List

class GamePlatformRepository:

  @staticmethod
  def insertGamePlatformRelation(game_id: int, platform_id: int) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO games_platforms(game_id, platform_id) VALUES (?, ?)", (game_id, platform_id))

      con.commit()
  
  @staticmethod
  def getPlatformsIDsByGameID(game_id: int) -> List[int]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      platforms_ids = cur.execute(f"SELECT platform_id FROM games_platforms WHERE game_id = ?", (game_id,)).fetchall()

      return list(map(lambda x: x[0], platforms_ids))
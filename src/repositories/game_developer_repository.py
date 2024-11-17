import sqlite3

from typing import List

class GameDeveloperRepository:

  @staticmethod
  def insertGameDeveloperRelation(game_id: int, developer_id: int) -> None:

    # game_id é o id do registro no banco, e não o id do jogo na API

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      cur.execute(f"INSERT INTO games_developers(game_id, developer_id) VALUES (?, ?)", (game_id, developer_id))

      con.commit()
  
  @staticmethod
  def getDevelopersIDsByGameID(game_id: int) -> List[int]:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      developers_ids = cur.execute(f"SELECT developer_id FROM games_developers WHERE game_id = ?", (game_id,)).fetchall()

      return list(map(lambda x: x[0], developers_ids))
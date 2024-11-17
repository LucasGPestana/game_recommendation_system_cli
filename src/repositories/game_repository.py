from src.game import Game

from src.repositories.developer_repository import DeveloperRepository
from src.repositories.genre_repository import GenreRepository
from src.repositories.platform_repository import PlatformRepository
from src.repositories.game_developer_repository import GameDeveloperRepository
from src.repositories.game_genre_repository import GameGenreRepository
from src.repositories.game_platform_repository import GamePlatformRepository

from typing import Dict, Any, Tuple, List
import sqlite3

class GameRepository:

  """
  Classe que permite realizar as operações de consulta com os dados obtidos da API da RAWG
  """

  @staticmethod
  def insertGame(game_data: Dict[str, Any]) -> None:

    with sqlite3.connect("some_games.db") as con:

      cur = con.cursor()

      # Criando o registro do jogo na tabela games
      cur.execute("INSERT INTO games(name, description, rating, image_url, released_date) VALUES (?, ?, ?, ?, ?)", (
        game_data.get('name'),
        game_data.get('description'), 
        game_data.get('rating'), 
        game_data.get('image_url'), 
        game_data.get('released')
        ))
    
      con.commit()

      context_game_data = GameRepository.getGameByName(game_data.get("name"))

      for genre in game_data.get("genres"):

        genre_data = GenreRepository.getGenreByName(genre)

        GameGenreRepository.insertGameGenreRelation(context_game_data[0], genre_data[0])

      
      for platform in game_data.get("platforms"):

        platform_data = PlatformRepository.getPlatformByName(platform)

        GamePlatformRepository.insertGamePlatformRelation(context_game_data[0], platform_data[0])

      
      for developer in game_data.get("developers"):

        developer_data = DeveloperRepository.getDeveloperByName(developer)

        # Como nem todos os desenvolvedores foram cadastrados, evita com que dê algum erro
        if developer_data:

          GameDeveloperRepository.insertGameDeveloperRelation(context_game_data[0], developer_data[0])
    
      con.commit() # Garante que os registros foram salvos no banco
  
  @staticmethod
  def getGameByName(name: str) -> Tuple[Any]:
  
    with sqlite3.connect("some_games.db") as con:
    
      cur = con.cursor()

      return cur.execute("SELECT id, name, description, rating, image_url, released_date FROM games WHERE name = ?", (name,)).fetchone()
  
  @staticmethod
  def getGameByID(game_id: int) -> Tuple[Any]:
  
    with sqlite3.connect("some_games.db") as con:
    
      cur = con.cursor()

      return cur.execute("SELECT id, name, description, rating, image_url, released_date FROM games WHERE id = ?", (game_id,)).fetchone()
  
  @staticmethod
  def getAllGamesID() -> List[str]:

     with sqlite3.connect("some_games.db") as con:
    
      cur = con.cursor()

      game_ids = list(map(lambda x: x[0], cur.execute("SELECT id FROM games").fetchall()))

      return game_ids
  
  @staticmethod
  def getGameObjectByID(game_id: int) -> Game:

    game_genres = [GenreRepository.getGenreByID(genre_id)[1] for genre_id in GameGenreRepository.getGenresIDsByGameID(game_id)]

    game_platforms = [PlatformRepository.getPlatformByID(platform_id)[1] for platform_id in GamePlatformRepository.getPlatformsIDsByGameID(game_id)]

    game_developers = [DeveloperRepository.getDeveloperByID(developer_id)[1] for developer_id in GameDeveloperRepository.getDevelopersIDsByGameID(game_id)]

    return Game(*GameRepository.getGameByID(game_id), 
                game_genres, 
                game_platforms, 
                game_developers)
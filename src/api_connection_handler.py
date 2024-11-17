import requests

import concurrent.futures
from typing import Dict, Any
from dotenv import load_dotenv
import os

from src.repositories.game_repository import GameRepository
from src.repositories.genre_repository import GenreRepository
from src.repositories.platform_repository import PlatformRepository
from src.repositories.developer_repository import DeveloperRepository

class APIConnectionHandler:

  """

  Representa um gerenciador de conexão com a API da RAWG

  Para mais informações sobre a API, visite esse site: https://rawg.io/apidocs

  """

  load_dotenv()

  URL = f"https://api.rawg.io/api/"
  API_KEY = os.getenv("API_KEY")

  @staticmethod
  def getGameDataByID(game_data) -> Dict[str, Any]:

    params = {
       
       "key": APIConnectionHandler.API_KEY

    }

    response = requests.get(url=f"{APIConnectionHandler.URL}/games/{game_data['id']}", params=params)

    if response.status_code == 200:

        return response.json()

  @staticmethod
  def insertGamesFromAPIToDB() -> None:

    params = {
        "key": APIConnectionHandler.API_KEY
    }
     
    response = requests.get(APIConnectionHandler.URL + "/games", params=params)

    if response.status_code == 200:
    
        num_pages = (response.json()["count"] // 40) + 1

        for page in range(1, num_pages + 1):
       
            params["page"] = page
            params["page_size"] = 40

            response = requests.get(APIConnectionHandler.URL + "/games", params=params)

            print(response.status_code)

            if response.status_code == 200:

                game_results = response.json()["results"]

                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

                    games_data = executor.map(APIConnectionHandler.getGameDataByID, game_results)

                    for game in games_data:

                        if game.get("id", None):

                            game_data = {
                            "name": game.get('name'),
                            "description": game.get('description') if game.get('description') else "",
                            "rating": game.get("rating"),
                            "image_url": game.get("background_image") if game.get("background_image") else "",
                            "released": game.get("released"),
                            "genres": [genre["name"] for genre in game.get("genres", [])],
                            "developers": [developer["name"] for developer in game.get("developers", [])],
                            "platforms": [platform["platform"]["name"] for platform in game.get("platforms", [])]
                            }
        
                            print(game["name"])
    
                            GameRepository.insertGame(game_data)
  
  @staticmethod
  def insertGenresFromAPIToDB() -> None:
     
    params = {
       "key": APIConnectionHandler.API_KEY
    }

    response = requests.get(APIConnectionHandler.URL + "/genres", params=params)

    if response.status_code == 200:

        num_pages = response.json()["count"]

        for page in range(1, num_pages + 1):

            params["page"] = page
            params["page_size"] = 5
    
            response = requests.get(APIConnectionHandler.URL + "/genres", params=params)

            if response.status_code == 200:

                genres_data = response.json()["results"]

                for genre in genres_data:

                    print(genre["name"])

                    GenreRepository.insertGenre({"name": genre["name"]})
  
  @staticmethod
  def insertPlatformsFromAPIToDB() -> None:

    params = {
       "key": APIConnectionHandler.API_KEY
    }
     
    response = requests.get(APIConnectionHandler.URL + "/platforms", params=params)

    if response.status_code == 200:

        num_pages = (response.json()["count"] // 40) + 1

    for page in range(1, num_pages + 1):

        params["page"] = page
        params["page_size"] = 40
    
        response = requests.get(APIConnectionHandler.URL + "/platforms", params=params)

        if response.status_code == 200:

            platforms_data = response.json()["results"]

            for platform in platforms_data:

                print(platform["name"])

                PlatformRepository.insertPlatform({"name": platform["name"]})
  
  @staticmethod
  def insertDevelopersFromAPIToDB() -> None:

    params = {
       "key": APIConnectionHandler.API_KEY
    }
      
    response = requests.get(APIConnectionHandler.URL + "/developers", params=params)

    if response.status_code == 200:

        num_pages = (response.json()["count"] // 40) + 1

        for page in range(1, num_pages + 1):

            params["page"] = page
            params["page_size"] = 40
    
            response = requests.get(APIConnectionHandler.URL, params=params)

            if response.status_code == 200:

                developers_data = response.json()["results"]

                for developer in developers_data:

                    print(developer["name"])

                    DeveloperRepository.insertDeveloper({"name": developer["name"]})
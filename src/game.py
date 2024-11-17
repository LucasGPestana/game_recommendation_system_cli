from typing import Iterable
import datetime

from utils.without_tags import getTextWithoutTags

class Game:

    def __init__(self,
                 game_id: int,
                 name: str,
                 description: str,
                 rating: float,
                 image_url: str,
                 released_date: str,
                 genres: Iterable[str],
                 platforms: Iterable[str],
                 developers: Iterable[str]):
        
        """
        Parâmetros:

          game_id: Id do jogo
          name: Nome do jogo
          description: Descrição do jogo
          rating: Nota do jogo
          image_url: Imagem do jogo
          released_date: Data de lançamento (formato yyyy-mm-dd)
          genres: Gêneros do jogo
          platforms: Plataformas do jogo
          developers: Empresas desenvolvedoras do jogo

        """

        self.__game_id = game_id
        self.__name = name
        self.__description = getTextWithoutTags(description)
        self.__rating = rating
        self.__image_url = image_url
        self.__released_date = datetime.datetime.strptime(released_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        self.__genres = genres
        self.__platforms = platforms
        self.__developers = developers

    @property
    def game_id(self) -> int:
        
        return self.__game_id
    
    @property
    def name(self) -> str:

        return self.__name
    
    @property
    def description(self) -> str:

        return self.__description
    
    @property
    def rating(self) -> float:
        
        return self.__rating
    
    @property
    def image_url(self) -> str:

        return self.__image_url
    
    @property
    def released_date(self) -> str:

        return self.__released_date

    @property
    def genres(self) -> Iterable[str]:
        
        return self.__genres

    @property
    def platforms(self) -> Iterable[str]:
        
        return self.__platforms

    @property
    def developers(self) -> Iterable[str]:
        
        return self.__developers

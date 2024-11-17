from src.game import Game

import re
from typing import List


class WeightCalculator:

    def __init__(self, game1: Game, game2: Game) -> None:

        """
        
        Parâmetros:

          game1: É o jogo definido como entrada
          game2: É o jogo a ser comparado com o jogo de entrada

        """

        self.setNameWeight(game1, game2)
        self.setGenreWeight(game1, game2)
        self.setPlatformWeight(game1, game2)
        self.setDeveloperWeight(game1, game2)
        self.setRatingWeight(game2)
    
    @property
    def name_weight(self) -> int:

        return self.__name_weight
    
    @property
    def gender_weight(self) -> int:

        return self.__genre_weight
    
    @property
    def rating_weight(self) -> int:

        return self.__rating_weight
    
    @property
    def platform_weight(self) -> int:

        return self.__platform_weight
    
    @property
    def developer_weight(self) -> int:

        return self.__rating_developer
    
    @property
    def total_weight(self) -> int:

        return sum([self.__name_weight, 
                    self.__genre_weight, 
                    self.__rating_weight, 
                    self.__platform_weight,
                    self.__developer_weight])

    def setNameWeight(self, game1: Game, game2: Game) -> None:
        """

        Define o peso do nome

        Cada parte do nome do game1 que é encontrado no game2 recebe +2 de peso

        """

        self.__name_weight: int = 0

        if game1.game_id != game2.game_id:

            sep_pattern: re.Pattern = re.compile("\s+")
            name_parts: List[str] = sep_pattern.split(game1.name)

            for name_part in name_parts:

                if name_part.lower() in game2.name.lower():

                    self.__name_weight += 1

    def setGenreWeight(self, game1: Game, game2: Game) -> None:
        """ 

        Define o peso dos gênero

        Cada gênero que aparece no game1 e no game2 recebe +7 de peso

        """

        self.__genre_weight: int = 0

        if game1.game_id != game2.game_id:

            for gender in game1.genres:

                if gender in game2.genres:

                    self.__genre_weight += 7

    def setRatingWeight(self, game2: Game) -> None:
        
        """

        Define o peso da nota. Esse peso serve como auxilio para que o game2, já próximo do game1 pelo nome e generos, tenha mais chance de ser recomendado caso sua nota seja maior.

        O peso da nota é dado pela parte inteira da operação aritmética (nota_game_2 * 1.5)

        """

        self.__rating_weight: int = 0

        if sum([self.__name_weight, self.__genre_weight]) != 0:

            self.__rating_weight = round(game2.rating * 1.5, 0)

    def setPlatformWeight(self, game1: Game, game2: Game) -> None:

        """
        Define o peso das plataformas do jogo.

        Cada platafroma que é a mesma em game1 e game2, será adicionado +2 de peso total
        """

        self.__platform_weight: int = 0

        if game1.game_id != game2.game_id:

            for platform in game1.platforms:

                if platform in game2.platforms:

                    self.__platform_weight += 2
    
    def setDeveloperWeight(self, game1: Game, game2: Game) -> None:

        """
        Define o peso das desenvolvedoras que distribuem o jogo.

        Cada desenvolvedora que é a mesma em game1 e game2, será adicionado +4 de peso total
        """

        self.__developer_weight: int = 0

        if game1.game_id != game2.game_id:

            for developer in game1.developers:

                if developer in game2.developers:

                    self.__developer_weight += 4
        

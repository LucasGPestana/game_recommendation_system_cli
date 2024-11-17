from typing import Dict, List, Tuple
import json
import os

from src.weight_calculator import WeightCalculator
from src.game import Game
from src.repositories.game_repository import GameRepository

class Graph:

  """

  Representa o grafo contendo os pesos das conexões entre cada jogo. Quanto maior o peso, mais próximo um jogo está do outro, e maior a probabilidade dele ser recomendado.

  """

  def __init__(self, graph_path: str="") -> None:

    """

    Parâmetros:

      graph_path: O caminho do arquivo json contendo o grafo
      
    """

    if graph_path:

      file_stream = open(graph_path, "r")

      self.adjacence_matrix = json.loads(file_stream.read())

      file_stream.close()

    else:
      
      self.adjacence_matrix: Dict[int, int] = {}

  def insertVert(self, game_id: int) -> None:

    """

    Insere um vértice dentro da matriz de adjacência do grafo, identificado pelo id do jogo passado como argumento.

    """

    # Adiciona o gameId como última chave do dicionário
    self.adjacence_matrix[game_id] = {}

    # Adiciona os pesos de cada relação dos jogos
    for game_id2 in self.adjacence_matrix.keys():

      game1: Game = GameRepository.getGameObjectByID(game_id)
      game2: Game = GameRepository.getGameObjectByID(game_id2)

      if game1 and game2:

        self.adjacence_matrix[game_id][game_id2] = WeightCalculator(game1, game2).total_weight

        # Adiciona também a relação no dicionário correspondente a cada jogo já registrado
        self.adjacence_matrix[game_id2][game_id] = WeightCalculator(game1, game2).total_weight
  
  def getRecommendedVerts(self, game_id: int) -> List[int]:

    """
    Recupera uma lista com os ids dos jogos mais recomendados a partir do id do jogo de entrada
    """

    verts: List[Tuple[int, int]] = sorted(self.adjacence_matrix[str(game_id)].items(), 
                                          key=lambda x: x[1], 
                                          reverse=True)
    
    # Remove todos os vértices que não possuem arestas conectando-as ao vértice do game_id
    verts = list(filter(lambda x: x[1] > 25, verts))

    return list(map(lambda x: x[0], verts))[:10]
  
  def save(self) -> None:

    """

    Salva o grafo em um arquivo JSON, para que vértices já definidos não sejam re-inseridos em uma nova sessão

    """

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                           "files", 
                           "graph.json"), 'w') as file_stream:

      file_stream.write(json.dumps(self.adjacence_matrix))
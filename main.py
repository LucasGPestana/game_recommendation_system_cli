from src.graph import Graph
from src.repositories.game_repository import GameRepository

import os
import argparse

if __name__ == "__main__":

  graph = Graph(os.path.join(os.path.dirname(__file__), "files", "graph.json") if "graph.json" in os.listdir(os.path.join(os.path.dirname(__file__), "files")) else "")

  """
  for game_id in GameRepository.getAllGamesID():

    if not game_id in graph.adjacence_matrix.keys():

      graph.insertVert(game_id)
  
  graph.save()
  """

  parser = argparse.ArgumentParser(prog="Game Recommendation System", description="Lista 10 jogos recomendados, a partir do nome de um jogo.")

  parser.add_argument("game_name", action="store", type=str, default="", help="O nome do jogo que deseja listar jogos recomendados.")

  namespace = parser.parse_args()

  if namespace.game_name:

    entry_game: str = namespace.game_name

    context_game = GameRepository.getGameByName(entry_game)

    if not context_game:

      os.sys.exit(f"Não foi encontrado nenhum jogo com o nome {entry_game}!")

    game_id: int = context_game[0]

    recommended_games_id = graph.getRecommendedVerts(game_id)

    filename: str = f"recommended_games_for_{'_'.join(entry_game.lower().split())}.txt"

    file_stream = open(os.path.join(os.path.dirname(__file__), "files", filename), 'w')

    for game_id in recommended_games_id:

      stream: str = ""

      recommended_game = GameRepository.getGameObjectByID(game_id)

      stream += "\n" + "---" * 20
      stream += f"\nID do Jogo: {recommended_game.game_id}"
      stream += f"\nNome do Jogo: {recommended_game.name}"
      stream += f"\nNota: {recommended_game.rating}"
      stream += f"\nData de Lançamento: {recommended_game.released_date}"
      stream += f"\nGêneros: {', '.join(recommended_game.genres)}"
      stream += f"\nPlataformas: {', '.join(recommended_game.platforms)}"
      stream += f"\nDesenvolvedores: {', '.join(recommended_game.developers)}"

      stream += "\n" + "---" * 20

      file_stream.write(stream)
    
    file_stream.close()

    print(f"O arquivo de recomendação se encontra em {os.path.join(os.path.dirname(__file__), 'files', filename)}")
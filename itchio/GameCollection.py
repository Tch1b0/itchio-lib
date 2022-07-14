from typing import List
from itchio.Session import Session
from itchio.Game import Game


class GameCollection:
    """
    Get information about your games
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self) -> List[Game]:
        """
        Get all of your games
        """
        data = self.session.get("my-games")
        games = []

        for game in data["games"]:
            games.append(
                Game.parse_from_dict(game, self.session)
            )

        return games

    def get_by_id(self, id: int) -> Game:
        data = self.session.get(f"game/{id}")
        return Game.parse_from_dict(data["game"], self.session)

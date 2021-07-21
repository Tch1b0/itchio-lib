from requests.sessions import session
from itchio.Session import Session
from itchio.Game import Game

class GameCollection:
    """
    Get information about your games
    """
    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self) -> list[Game]:
        data = self.session.get("my-games")
        games = []

        for game in data["games"]:
            games.append(
                Game.parse_from_dict(game, self.session)
            )

        return games
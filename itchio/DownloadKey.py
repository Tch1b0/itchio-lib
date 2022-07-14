from itchio.User import User


class DownloadKey:
    def __init__(
            self,
            id: int,
            created_at: str,
            downloads: int,
            key: str,
            game_id: int,
            owner: User) -> None:

        self.id = id
        self.created_at = created_at
        self.downloads = downloads
        self.key = key
        self.game_id = game_id
        self.owner = owner

    @classmethod
    def parse_from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            created_at=data["created_at"],
            downloads=data["downloads"],
            key=data["key"],
            game_id=data["game_id"],
            owner=User.parse_from_dict(data["owner"])
        )

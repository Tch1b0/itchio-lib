from itchio.Session import Session


class User:
    """
    An Object representing the User ressource
    """
    def __init__(
        self,
        username: str,
        gamer: bool,
        display_name: str,
        cover_url: str,
        url: str,
        press_user: bool,
        developer: bool,
        id: int,
        session: Session):
        self.username = username
        self.gamer = gamer
        self.display_name = display_name
        self.cover_url = cover_url
        self.url = url
        self.press_user = press_user
        self.developer = developer
        self.id = id
        self.session = session

    def sync(self) -> object:
        """
        Sync this object with the information in the API
        """
        data = self.session.get("me")
        new_user = self.parse_from_dict(data["user"], self.session)
        self.__dict__.update(new_user.__dict__)

    @staticmethod
    def parse_from_dict(data: dict, session: Session) -> object:
        # If there is no 'display_name', the value is the same as the username
        if "display_name" not in data:
            data["display_name"] = data["username"]

        return User(
            username = data["username"],
            gamer = data["gamer"],
            display_name = data["display_name"],
            cover_url = data["cover_url"],
            url = data["url"],
            press_user = data["press_user"],
            developer = data["developer"],
            id = data["id"],
            session = session
        )
from itchio.Session import Session
from itchio.user.User import User

class UserCollection:
    def __init__(self, session: Session) -> None:
        self.session = session

    def me(self) -> User:
        """
        Get your account / The owner of the token
        """
        data = self.session.get("me")
        return User.parse_from_dict(data["user"])
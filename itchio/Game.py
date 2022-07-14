from typing import List, Union
from itchio.DownloadKey import DownloadKey
from itchio.User import User
from itchio.Purchase import Purchase
from itchio.Session import Session
from itchio.Earnings import Earnings


class Game:
    def __init__(
            self,
            cover_url: str,
            created_at: str,
            downloads_count: int,
            id: int,
            min_price: int,
            p_android: bool,
            p_linux: bool,
            p_osx: bool,
            p_windows: bool,
            published: bool,
            published_at: str,
            purchase_count: Union[int, None],
            short_text: str,
            title: str,
            type: str,
            url: str,
            views_count: int,
            earnings: Union[dict, None],
            session: Session):

        self.cover_url = cover_url
        self.created_at = created_at
        self.downloads_count = downloads_count
        self.id = id
        self.min_price = min_price
        self.p_android = p_android
        self.p_linux = p_linux
        self.p_osx = p_osx
        self.p_windows = p_windows
        self.published = published
        self.published_at = published_at
        self.purchase_count = purchase_count
        self.short_text = short_text
        self.title = title
        self.type = type
        self.url = url
        self.views_count = views_count

        if earnings == None:
            self.earnings = None
        else:
            self.earnings = []
            for entry in earnings:
                self.earnings.append(
                    Earnings.parse_from_dict(entry)
                )

        self.session = session

    def purchases(self, user: Union[str, int, User]) -> List[Purchase]:
        """
        Get the purchases of this Game

        Parameters:
            `user`: Either the id, the User object or the email of the User
        """

        param = ""

        if type(user) == User:
            param = "user_id"
            name = User.id
        elif type(user) == str:
            param = "email"
            name = user
        elif type(user) == int:
            param = "user_id"
            name = user
        else:
            raise ValueError(
                f"Parameter user has either to be type of str, int or User, not {type(user)}")

        data = self.session.get(f"game/{self.id}/purchases?{param}={name}")
        purchases = []
        for purchase in data["purchases"]:
            purchases.append(
                Purchase.parse_from_dict(purchase)
            )

        return purchases

    def download_keys(self, user_or_key: Union[str, int, User]) -> DownloadKey:
        """
        Get a download key of this Game

        Parameters:
            `user_or_key`: Either the id of the User, the email address of the User, the User object or the download key
        """

        param = ""

        if type(user_or_key) == User:
            param = "user_id"
            name = user_or_key.id
        elif type(user_or_key) == int:
            param = "user_id"
            name = user_or_key
        elif type(user_or_key) == str and "@" in user_or_key:
            param = "email"
            name = user_or_key
        elif type(user_or_key) == str:
            param = "download_key"
            name = user_or_key
        else:
            raise ValueError(
                f"Parameter user_or_key has either to be type of str, int or User, not {type(user_or_key)}")

        data = self.session.get(f"game/{self.id}/download_keys?{param}={name}")
        if "errors" in data:
            raise Exception(data["errors"])
        else:
            return DownloadKey.parse_from_dict(data["download_key"])

    @staticmethod
    def parse_from_dict(data: dict, session: Session) -> object:
        if "purchase_count" not in data:
            data["purchase_count"] = None
        if "earnings" not in data:
            data["earnings"] = None
        if "downloads_count" not in data:
            data["downloads_count"] = None
        if "published" not in data:
            data["published"] = None
        if "views_count" not in data:
            data["views_count"] = None
        if "title" not in data:
            data["title"] = None
        if "cover_url" not in data:
            data["cover_url"] = None
        if "created_at" not in data:
            data["created_at"] = None
        if "id" not in data:
            data["id"] = None
        if "min_price" not in data:
            data["min_price"] = None
        if "cover_url" not in data:
            data["cover_url"] = None
        if "published_at" not in data:
            data["published_at"] = None
        if "short_text" not in data:
            data["short_text"] = None

        return Game(
            cover_url=data["cover_url"],
            created_at=data["created_at"],
            downloads_count=data["downloads_count"],
            id=data["id"],
            min_price=data["min_price"],
            p_android=data["p_android"],
            p_linux=data["p_linux"],
            p_osx=data["p_osx"],
            p_windows=data["p_windows"],
            published=data["published"],
            published_at=data["published_at"],
            purchase_count=data["purchase_count"],
            short_text=data["short_text"],
            title=data["title"],
            type=data["type"],
            url=data["url"],
            views_count=data["views_count"],
            earnings=data["earnings"],
            session=session
        )

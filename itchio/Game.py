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
        purchase_count: int or None,
        short_text: str,
        title: str,
        type: str,
        url: str,
        views_count: int,
        earnings: dict or None):

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


    @staticmethod
    def parse_from_dict(data: dict):
        if "purchase_count" not in data:
            data["purchase_count"] = None
        if "earnings" not in data:
            data["earnings"] = None

        return Game(
            cover_url = data["cover_url"],
            created_at = data["created_at"],
            downloads_count = data["downloads_count"],
            id = data["id"],
            min_price = data["min_price"],
            p_android = data["p_android"],
            p_linux = data["p_linux"],
            p_osx = data["p_osx"],
            p_windows = data["p_windows"],
            published = data["published"],
            published_at = data["published_at"],
            purchase_count = data["purchase_count"],
            short_text = data["short_text"],
            title = data["title"],
            type = data["type"],
            url = data["url"],
            views_count = data["views_count"],
            earnings = data["earnings"]
        )
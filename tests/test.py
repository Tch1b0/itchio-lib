import unittest
import itchio
import requests_mock

class TestUser(unittest.TestCase):
    def test_get_me(self):
        with requests_mock.Mocker() as m:
            m.get("https://itch.io/api/1/1234/me", json = {
                "user": {
                    "username": "fasterthanlime",
                    "gamer": True,
                    "display_name": "Amos",
                    "cover_url": "https://img.itch.zone/aW1hZ2UyL3VzZXIvMjk3ODkvNjkwOTAxLnBuZw==/100x100%23/JkrN%2Bv.png",
                    "url": "https://fasterthanlime.itch.io",
                    "press_user": True,
                    "developer": True,
                    "id": 29789
                }
            })
            session = itchio.Session("1234")
            userCollection = itchio.UserCollection(session)
            user = userCollection.me()
            self.assertTrue(user.username == "fasterthanlime")

    def test_get_all_games(self):
        with requests_mock.Mocker() as m:
            m.get("https://itch.io/api/1/1234/my-games", json = {
                "games":[
                    {
                        "cover_url":"http:\/\/img.itch.io\/aW1hZ2UvMy8xODM3LnBuZw==\/315x250%23\/y2uYQI.png",
                        "created_at":"2013-03-03 23:02:14",
                        "downloads_count":109,
                        "id":3,
                        "min_price":0,
                        "p_android":False,
                        "p_linux":True,
                        "p_osx":True,
                        "p_windows":True,
                        "published":True,
                        "published_at":"2013-03-03 23:02:14",
                        "purchases_count":4,
                        "short_text":"Humans have been colonizing planets. It's time to stop them!",
                        "title":"X-Moon",
                        "type":"default",
                        "url":"http:\/\/leafo.itch.io\/x-moon",
                        "views_count":2682,
                        "earnings":[
                            {
                            "currency":"USD",
                            "amount_formatted":"$50.47",
                            "amount":5047
                            }
                        ]
                    }
                ]
            })

            session = itchio.Session("1234")
            gameCollection = itchio.GameCollection(session)
            self.assertTrue(gameCollection.all()[0].id == 3)

unittest.main()
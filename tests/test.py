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

unittest.main()
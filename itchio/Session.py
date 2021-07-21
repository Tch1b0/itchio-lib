import requests

class Session:
    """
    A session object that is used for making requests
    """
    def __init__(self, key: str, url: str = "https://itch.io/api/1"):
        self.key = key
        self.url = f"{url}/{key}/"
        self.session = requests.session()
    
    def get(self, route: str) -> dict:
        """
        Get a certain ressource
        """
        response = self.session.get(f"{self.url}{route}")
        if response.ok:
            return response.json()
        else:
            raise Exception(f"Response of {self.url}{route} was {response.status_code}")
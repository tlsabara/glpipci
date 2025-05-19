import httpx

class BasicAuth:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def auth(self) -> str:
        return httpx.BasicAuth(username=self.username, password=self.password)

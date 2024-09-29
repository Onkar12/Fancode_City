import requests
from src.config import CONFIG

class APIClient:
    BASE_URL = CONFIG['api_base_url']

    @staticmethod
    def fetch(endpoint):
        response = requests.get(f"{APIClient.BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()

    @classmethod
    def get_users(cls):
        return cls.fetch("users")

    @classmethod
    def get_todos(cls):
        return cls.fetch("todos")

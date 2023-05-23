

import requests


class JserviceDAO:
    def get_questions(self, number: int) -> list:
        data = requests.get(f"https5://jservice.io/api/random?count={number}")
        return data.json()



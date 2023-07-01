import pytest
import requests

def test_status_code():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url)
    assert response.status_code == 200

def test_trainer_id():
    url = "https://api.pokemonbattle.me:9104/trainers?trainer_id=4387"
    response = requests.get(url)
    response = response.json()
    assert response["id"] == "4387"
import requests

data_pokemons = {
    "name": "generate",
    "photo": "generate"
}
response = requests.post("https://api.pokemonbattle.me:9104/pokemons", 
                         headers = {"trainer_token":"d591a68c6cf5c4b61900486fac2f4c98" ,"Content-Type":"application/json"}, 
                         json = data_pokemons)
print(response.text)

data_putpokem = {
    "pokemon_id": "15101",
    "name": "Pythonkill",
    "photo": "https://dolnikov.ru/pokemons/albums/838.png"
}
response = requests.put("https://api.pokemonbattle.me:9104/pokemons", 
                         headers = {"trainer_token":"d591a68c6cf5c4b61900486fac2f4c98" ,"Content-Type":"application/json"}, 
                         json = data_putpokem)
print(response.text)

data_pokeboll = {"pokemon_id":"15102"}
response = requests.post("https://api.pokemonbattle.me:9104/trainers/add_pokeball", 
                         headers = {"trainer_token":"d591a68c6cf5c4b61900486fac2f4c98" ,"Content-Type":"application/json"}, 
                         json = data_pokeboll)
print(response.text)

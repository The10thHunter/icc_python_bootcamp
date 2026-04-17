import requests as r 

class Pokemon: 
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.base_exp = data["base_experience"]
        self.height = data["height"]
    def printStat(self): 
        print(f"Pokemon at id {self.id} with name {self.name} has base experience {self.base_exp} and height {self.height}")

for var in range(1, 100):
    response = r.get(f"https://pokeapi.co/api/v2/pokemon/{var}/")
    data = response.json()
    poke = Pokemon(data)
    poke.printStat()


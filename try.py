import json
path = 'src/assets/saves/main.json'
with open(path, "r") as file:
    data = json.load(file)
    print(list(data.keys()))

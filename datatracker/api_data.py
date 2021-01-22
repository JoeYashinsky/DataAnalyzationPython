import requests
import json
from types import SimpleNamespace

response = requests.get('https://api.dccresource.com/api/games')
games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

for game in games:
    print(game.name)

#with open('games.txt', "w") as json_file:
 #   json.dump(games, json_file, indent=4, sort_keys=True)







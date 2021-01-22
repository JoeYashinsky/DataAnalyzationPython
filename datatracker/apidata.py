from types import SimpleNamespace

import json
import requests

response = requests.get('https://api.dccresource.com/api/games')

games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

for game in games:
    print(game[0])

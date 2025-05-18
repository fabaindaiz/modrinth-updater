from src.library.utils import load_env
load_env(".env.yaml")

import urllib.parse
import asyncio
from pprint import pprint
from src.library.api.client.modrinth import ModrinthAPI, ModrinthCDN
modrinthAPI = ModrinthAPI()
modrinthCDN = ModrinthCDN()

response = asyncio.run(modrinthAPI.project_dependencies("oh-the-biomes-weve-gone"))
parsed = [mod["slug"] for mod in response["projects"]]
#pprint(parsed)

response = asyncio.run(modrinthAPI.project_versions("oh-the-biomes-weve-gone", loaders=["forge", "neoforge"], game_versions=["1.20.1"]))
pprint(response)

url: str = response[0]["files"][0]["url"]
name = urllib.parse.unquote(url.split("/")[-1])

file = asyncio.run(modrinthCDN.download_file(url))
with open(name, "wb") as f:
    f.write(file)
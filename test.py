from src.library.utils import load_env, name_from_url
load_env(".env.yaml")

from src.library.api.client.modrinth import ModrinthAPI, ModrinthCDN
from src.library.api.client.pterodactyl import PterodactylAPI
modrinthAPI = ModrinthAPI()
modrinthCDN = ModrinthCDN()
pterodactylAPI = PterodactylAPI()

import os
import asyncio
from pprint import pprint

# response = asyncio.run(modrinthAPI.project_dependencies("oh-the-biomes-weve-gone"))
# parsed = [mod["slug"] for mod in response["projects"]]
# #pprint(parsed)

# response = asyncio.run(modrinthAPI.project_versions("oh-the-biomes-weve-gone", loaders=["forge", "neoforge"], game_versions=["1.20.1"]))
# pprint(response)

# url: str = response[0]["files"][0]["url"]
# filename = os.path.join("data", name_from_url(url))

# file = asyncio.run(modrinthCDN.download_file(url))
# with open(filename, mode="wb") as f:
#     f.write(file)

response = asyncio.run(pterodactylAPI.servers_list())
pprint(response)
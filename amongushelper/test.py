import asyncio, time
from typing import Union
from difflib import get_close_matches

maps = {
    "polus" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png",
    "skeld" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg",
    "mira" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png"
}
map_name = input("Enter map name:\n")
print (maps[map_name])
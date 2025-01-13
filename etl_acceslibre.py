import json
from pprint import pprint
import os

len(os.listdir("./data/acceslibre"))

with open("./data/acceslibre/results-acceslibre-0.json", "r") as f:
    j = json.loads(f.read())

    pprint(j)

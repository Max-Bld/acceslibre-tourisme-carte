import requests
import json

headers = {
    "Authorization": "Api-Key 0GLZTHG3.lb6vfjqyFuPseAEoxjgftABZNgwKhZM5"
}

endpoint = "https://acceslibre.beta.gouv.fr/api/erps"

parameters = {
    "zone": "0.999665,47.441165,1.675203,47.816915",
    "page_size": 100,
    "clean": "true"
}

n = 0

r = requests.get(endpoint, headers=headers, params=parameters)

with open("data/results-acceslibre-0.json", "w") as f:
    f.write(json.dumps(r.json()['results']))

while r.json()['next']:
    n += 1
    r = requests.get(r.json()['next'], headers=headers)
    with open(f"data/results-acceslibre-{n}.json", "w") as f:
        f.write(json.dumps(r.json()['results']))
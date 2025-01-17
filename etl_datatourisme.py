import pandas as pd
import json
from tqdm import tqdm
import os

root_path = os.getcwd()[:-20]

def etl_datatourisme():
    datatourisme = f"{root_path}/datatourisme/"

    columns = ['type', 'name', 'lat', 'lon', 'city']

    df = pd.DataFrame(
        columns=columns
    )

    with open(f"{datatourisme}/index.json", "r") as f:
        j = json.loads(f.read())

    for id in tqdm(range(len(j))):
        with open(f"{datatourisme}/objects/" + j[id]['file'], "r") as f:
            poi = json.loads(f.read())

            lat = poi['isLocatedAt'][0]['schema:geo']['schema:latitude']
            lon = poi['isLocatedAt'][0]['schema:geo']['schema:longitude']
            name = poi['rdfs:label']['fr'][0].replace("'", " ")
            city = poi['isLocatedAt'][0]['schema:address'][0]['schema:addressLocality']
            type = poi['@type'][0]

            try:
                accessibility = poi['reducedMobilityAccess']
            except:
                accessibility = "False"

        df.loc[id] = [type, name, lat, lon, city]

    df.to_pickle(f"{root_path}/visualisation-carte/data/datatourisme.pkl")
    return {'status': 'success'}
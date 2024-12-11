import folium
from folium.plugins import HeatMap, MarkerCluster

import geopandas as gpd
import pandas as pd
from tqdm import tqdm

from etl_datatourisme import etl_datatourisme
from geo_functions import highlight_feature

# Etl

import os
if len(os.listdir('data/')) == 0:
    print("Directory is empty")
    result = etl_datatourisme()
    print(result)

# Data

    # territoires

territoires = "/home/maximeb/pro/eonax/hackathon/france-geojson/regions/centre-val-de-loire/cantons-centre-val-de-loire.geojson"

territoires_gdf = gpd.read_file(territoires)

    # datatourisme

datatourisme = pd.read_pickle("data/datatourisme.pkl")

datatourisme_series= gpd.points_from_xy(datatourisme.lon, datatourisme.lat)
datatourisme_gdf = gpd.GeoDataFrame(datatourisme, geometry=datatourisme_series)
datatourisme_gdf.crs = "EPSG:4326"

# filtres

# territoires_mask = territoires_gdf['nom'].str.contains('Bourges') == True
# territoires_gdf = territoires_gdf[territoires_mask]
#
datatourisme_mask = datatourisme_gdf['type']=='PlaceOfInterest'
datatourisme_gdf = datatourisme_gdf[datatourisme_mask]


print(datatourisme_gdf)
#
# datatourisme_gdf['within'] = territoires_gdf.contains(datatourisme_gdf)
#
# mask = datatourisme_gdf['within'] == "False"


# Geo Viz

style = {'fillColor': '#ff0000', 'weight': 2, 'color': 'black'}
highlight = {'fillColor': '#111000', 'weight': 2, 'color': 'white'}

m = folium.Map([47.7, 0], zoom_start=6)

folium.GeoJson(
    data=territoires_gdf,
    name="Territoires",
    style_function=lambda feature: style,
    highlight_function=lambda x: {"fillOpacity": 0.4},
    tooltip=folium.GeoJsonTooltip(fields=["nom", "code"]),
    zoom_on_click=True
).add_to(m)

popup = folium.GeoJsonPopup(
    fields=["name", "type", "city"],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

folium.GeoJson(
    data=datatourisme_gdf,
    name="POIs",
    marker=folium.CircleMarker(fillColor='#f5c211', fill_opacity=0.4, color="black", weight=1),
    #marker=folium.Circle(radius=1000, fillColor='#333000', fill_opacity=0.4, color="white", weight=2),
    tooltip=folium.GeoJsonTooltip(fields=["name", "type", "city"]),
    popup=popup,
    zoom_on_click=True
).add_to(m)

m.save('map.html')
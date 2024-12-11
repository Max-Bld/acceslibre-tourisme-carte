from shapely.geometry import Point

def latlon_to_geojson_point(lon, lat):
    points = [Point(x, y) for x, y in zip(df['lon'], df['lat'])]

def highlight_feature(feature):
    if feature['type'] == 'PlaceOfInterest':
        return {"radius": 8}
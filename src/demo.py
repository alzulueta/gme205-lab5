from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road


parcel_geom = Polygon([
    (121.0583,14.6545),
    (121.0589,14.6545),
    (121.0589,14.655),
    (121.0583,14.655)
])

building_geom = Polygon([
    (121.0575,14.6538),
    (121.0579,14.6538),
    (121.0579,14.6541),
    (121.0575,14.6541)
])

road_geom = LineString([
    (121.0568,14.655),
    (121.0595,14.655)
])


parcel = Parcel(parcel_geom)
building = Building(building_geom, floors=3)
road = Road(road_geom, width=8)


features = [parcel, building, road]


for f in features: # with AI assistance
    print(type(f).__name__, f.effective_area())
import json
from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road
import math

# Conversion factors (with AI assistance)
LAT_TO_M = 111_000  # meters per degree latitude
def lon_to_m(lat_deg):
    return 111_000 * math.cos(math.radians(lat_deg))

def scale_coordinates(coords):
    """Convert lat/lon coordinates to meters."""
    return [(lon*lon_to_m(lat), lat*LAT_TO_M) for lon, lat in coords]

def load_data():
    with open("../data/spatial_features.json") as f:
        return json.load(f)

def create_objects(data):
    features = []
    for item in data:
        ftype = item["type"]
        geom_type = item["geometry"]["type"]
        coords = item["geometry"]["coordinates"]

        # Scale coordinates
        if geom_type == "Polygon":
            geometry = Polygon(scale_coordinates(coords[0]))
        elif geom_type == "LineString":
            geometry = LineString(scale_coordinates(coords))
        else:
            continue

        # Create objects
        if ftype == "Parcel":
            obj = Parcel(geometry)
            obj.feature_id = item.get("parcel_id", "Unknown")
        elif ftype == "Building":
            floors = item.get("floors", 1)
            obj = Building(geometry, floors)
            obj.feature_id = item.get("building_id", "Unknown")
        elif ftype == "Road":
            width_m = item.get("width", 1)
            obj = Road(geometry, width_m)
            obj.feature_id = item.get("road_id", "Unknown")
        else:
            continue

        features.append(obj)
    return features

def demonstrate_polymorphism(features):
    print("\n--- Polymorphism Demonstration ---\n")
    for f in features:
        print(f"{type(f).__name__} {f.feature_id} effective area: {round(f.effective_area(),2)}")

def compute_total_area(features):
    return sum(f.effective_area() for f in features)

def main():
    data = load_data()
    features = create_objects(data)

    if not features:
        print("No spatial features found")
        return

    # Polymorphism demo
    demonstrate_polymorphism(features)

    # Total area
    total_area = compute_total_area(features)
    print("\nTotal Effective Area:", round(total_area,2))

if __name__ == "__main__":
    main()
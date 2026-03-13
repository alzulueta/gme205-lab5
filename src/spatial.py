from shapely.geometry import Polygon, LineString

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry
        self.feature_id = None

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError


class Parcel(SpatialObject):
    def effective_area(self):
        # Just return polygon area
        return self.geometry.area


class Building(SpatialObject):
    def __init__(self, geometry, floors):
        super().__init__(geometry)
        self.floors = floors

    def effective_area(self):
        # Polygon area multiplied by floors
        return self.geometry.area * self.floors


class Road(SpatialObject):
    def __init__(self, geometry, width):
        super().__init__(geometry)
        self.width = width

    def effective_area(self):
        # Use line length * width
        return self.geometry.length * self.width
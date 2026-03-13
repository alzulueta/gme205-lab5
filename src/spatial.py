from shapely.geometry import Polygon, LineString

class SpatialObject:

    def __init__(self, geometry):
        self.geometry = geometry

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError
    
class Parcel(SpatialObject):

    def effective_area(self):
        return self.geometry.area


class Building(SpatialObject):

    def __init__(self, geometry, floors):
        super().__init__(geometry)
        self.floors = floors

    def effective_area(self):
        return self.geometry.area * self.floors


class Road(SpatialObject):
    
    def __init__(self, geometry, width):
        super().__init__(geometry)
        self.width = width

    def effective_area(self):
        return self.geometry.buffer(self.width).area
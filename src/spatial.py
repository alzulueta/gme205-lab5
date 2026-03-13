class SpatialObject:

    def __init__(self, geometry):
        self.geometry = geometry

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError
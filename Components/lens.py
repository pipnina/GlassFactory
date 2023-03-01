from Components.component import Component, ComponentType
from Components.surface_properties import SurfaceProperties


class Lens(Component):
    def __init__(self,
                 component_name: str,
                 parent=None,
                 diameter: float = 30,
                 thickness: float = 5,
                 surfaces: tuple[SurfaceProperties, SurfaceProperties] = None):
        if component_name is None:
            component_name = "New Lens"

        super().__init__(component_name=component_name, component_type=ComponentType.Lens, parent=parent, component_UUID=None)

        # If no surfaces are provided, create a pair
        if surfaces is None:
            surfaces = (SurfaceProperties(), SurfaceProperties())
        self.surfaces = surfaces

        self.diameter = diameter
        self.thickness = thickness

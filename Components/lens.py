from dataclasses import dataclass
from Components.component import Component


@dataclass
class SurfaceProperties:
    focal_length: 100
    conic_constant: 0
    is_flat: False
    is_reflective: False

    def __init__(self):
        super().__init__()
        pass

    def __init__(self, length: float, constant: float, flat: bool, reflective: bool):
        super().__init__()
        self.focal_length = length
        self.conic_constant = constant
        self.is_flat = flat
        self.is_reflective = reflective


class Lens(Component):
    #properties = {"diameter": 30, "thickness": 5, "surfaces": [SurfaceProperties]}
    #diameter = 30
    #thickness = 5
    #surfaces: [SurfaceProperties] = []

    def __init__(self):
        super().__init__()
        self.properties["surfaces"].append(SurfaceProperties())

    def __init__(self, surface1: SurfaceProperties, surface2: SurfaceProperties, diameter: float, thickness: float):
        super().__init__()
        #self.surfaces.append(surface1)
        #self.surfaces.append(surface2)
        #self.diameter = diameter
        #self.thickness = thickness
        self.properties["surfaces"].append(surface1)
        self.properties["surfaces"].append(surface2)
        self.properties["diameter"] = diameter
        self.properties["thickness"] = thickness

    def getProperties(self):
        return self.properties

    def setProperty(self, component_property: [str], value):
        self.properties[component_property] = value


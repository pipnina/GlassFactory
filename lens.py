from dataclasses import dataclass


@dataclass
class SurfaceProperties:
    focal_length: 100
    conic_constant: 0
    is_flat: False
    is_reflective: False

    def __init__(self, length: float, constant: float, flat: bool, reflective: bool):
        self.focal_length = length
        self.conic_constant = constant
        self.is_flat = flat
        self.is_reflective = reflective

class Lens:
    diameter = 30
    thickness = 5
    surface1 = SurfaceProperties
    surface2 = SurfaceProperties

    def __init__(self, surface1: SurfaceProperties, surface2: SurfaceProperties, diameter: float, thickness: float):
        self.surface1 = surface1
        self.surface2 = surface2
        self.diameter = diameter
        self.thickness = thickness


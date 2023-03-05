from dataclasses import dataclass


@dataclass
class SurfaceProperties:
    focal_length: float = 100
    conic_constant: float = 0
    is_flat: bool = False
    is_reflective: bool = False



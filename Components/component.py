# Lens, Baffle, Prism, Camera, Focuser, Light, Group
from dataclasses import dataclass
from enum import Enum
from PySide6.QtWidgets import QListWidgetItem


class ComponentType(Enum):
    Lens = 1
    Baffle = 2
    Prism = 3
    Camera = 4
    Focuser = 5
    Light = 6
    Group = 7


@dataclass
class Component:
    component_name: str
    component_type: ComponentType
    component_UUID: None
    parent: str
    x: float = 0
    y: float = 0
    z: float = 0
    xr: float = 0
    yr: float = 0

    def get_ui(self):
        q_list_widget_items = []
        q_list_widget_items.append(QListWidgetItem("Hello"))

        return q_list_widget_items

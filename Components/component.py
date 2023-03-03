# Lens, Baffle, Prism, Camera, Focuser, Light, Group
from dataclasses import dataclass
from enum import Enum
from PySide6.QtWidgets import QListWidgetItem, QHBoxLayout, QCheckBox, QWidget, QLabel, QLayout, QLineEdit


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
    # yr: float = 0

    def get_ui(self):
        q_list_widget_items = []

        # component_name list element
        name_widget = self.make_config_widget("Name: ")
        name_textbox = QLineEdit()
        name_textbox.setText(self.component_name)
        name_textbox.editingFinished.connect(lambda: self.name_event_function(name_textbox.displayText()))
        name_widget.layout().addWidget(name_textbox)
        q_list_widget_items.append(name_widget)

        # X position list element
        x_widget = self.make_config_widget("X: ")
        x_textbox = QLineEdit()
        x_textbox.setText(str(self.x))
        x_textbox.editingFinished.connect(lambda: self.x_event_function(x_textbox.displayText()))
        x_widget.layout().addWidget(x_textbox)
        q_list_widget_items.append(x_widget)

        return q_list_widget_items

    def make_config_widget(self, label_name: str):
        widget = QWidget()
        layout = QHBoxLayout()
        list_item = QLabel(label_name)

        layout.addWidget(list_item)
        layout.addStretch()
        layout.setSizeConstraint(QLayout.SetFixedSize)
        widget.setLayout(layout)

        return widget

    def name_event_function(self, widgetbox):
        self.component_name = widgetbox

    def x_event_function(self, widgetbox):
        try:
            self.x = float(widgetbox)
        except ValueError:
            print("You need to enter a number!")

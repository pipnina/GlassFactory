# Lens, Baffle, Prism, Camera, Focuser, Light, Group
from dataclasses import dataclass
from functools import partial
from enum import Enum
from PySide6.QtWidgets import QListWidgetItem, QHBoxLayout, QCheckBox, QWidget, QLabel, QLayout, QLineEdit
from event_manager import raise_event, Event

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
    #z: float = 0
    xr: float = 0
    # yr: float = 0

    def get_ui(self):
        q_list_widget_items = []

        # component_name list element
        name_widget = self._make_config_widget("Name: ", self.component_name, self._on_name_changed)
        name_widget.itemAt(0).widget()
        name_widget.itemAt(1).widget().setText(str(self.component_name))
        # textbox.editingFinished.connect(lambda: function_ptr(textbox))
        q_list_widget_items.append(name_widget)

        # X position list element
        x_widget = self._make_config_widget("X: ", self.x, self._on_x_value_changed)
        q_list_widget_items.append(x_widget)

        # y position list element
        y_widget = self._make_config_widget("Y: ", self.y, self._on_y_value_changed)
        q_list_widget_items.append(y_widget)

        # rotation list element
        rotation_widget = self._make_config_widget("Rotation: ", self.xr, self._on_rotation_value_changed)
        q_list_widget_items.append(rotation_widget)

        return q_list_widget_items

    @staticmethod
    def _make_config_widget(label_name: str, variable, function_ptr):
        # widget = QWidget()
        layout = QHBoxLayout()
        list_item = QLabel(label_name)
        list_item.setMinimumSize(130, 10)
        textbox = QLineEdit()
        textbox.setText(str(variable))
        textbox.editingFinished.connect(partial(function_ptr, textbox))

        layout.addWidget(list_item)
        layout.addWidget(textbox)
        layout.addStretch()
        layout.setSizeConstraint(QLayout.SetFixedSize)
        # widget.setLayout(layout)

        return layout  # widget


    # Event handlers for handling user input to the UI created
    def _on_name_changed(self, widgetbox):
        self.component_name = widgetbox.displayText()
        raise_event(Event.ComponentChanged)

    def _on_x_value_changed(self, widgetbox):
        try:
            self.x = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.x))

    def _on_y_value_changed(self, widgetbox):
        try:
            self.y = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.y))

    def _on_rotation_value_changed(self, widgetbox):
        try:
            self.xr = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.xr))

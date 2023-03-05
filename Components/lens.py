from Components.component import Component, ComponentType
from Components.surface_properties import SurfaceProperties
from PySide6.QtWidgets import QLineEdit
from event_manager import raise_event, Event


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

    # continue the get_ui method from the parent class Component
    def get_ui(self):
        q_list_widget_items = super().get_ui()
        print("This is a lens")

        # diameter list element
        diameter_widget = self._make_config_widget("Diameter: ", self.diameter, self._on_diameter_value_changed)
        q_list_widget_items.append(diameter_widget)

        # thickness list element
        thickness_widget = self._make_config_widget("Thickness: ", self.thickness, self._on_thickness_value_changed)
        q_list_widget_items.append(thickness_widget)

        return q_list_widget_items

    def _on_diameter_value_changed(self, widgetbox):
        try:
            self.diameter = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.diameter))

    def _on_thickness_value_changed(self, widgetbox):
        try:
            self.thickness = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.thickness))


from Components.component import Component, ComponentType
from Components.surface_properties import SurfaceProperties
from event_manager import raise_event, Event


class Lens(Component):
    def __init__(self,
                 component_name: str,
                 x=0,
                 y=0,
                 xr=0,
                 diameter: float = 30,
                 thickness: float = 5,
                 refractive_index=1.414,
                 surfaces: tuple[SurfaceProperties, SurfaceProperties] = None):

        if component_name is None:
            component_name = "New Lens"

        super().__init__(component_name=component_name,
                         x=x,
                         y=y,
                         xr=xr)

        self.component_type = ComponentType.Lens
        # If no surfaces are provided, create a pair
        if surfaces is None:
            surfaces = (SurfaceProperties(), SurfaceProperties())
        self.surfaces = surfaces

        self.diameter = diameter
        self.thickness = thickness
        self.refractive_index = refractive_index

    # continue the get_ui method from the parent class Component
    def get_ui(self):
        q_list_widget_items = super().get_ui()

        # diameter list element
        diameter_widget = self._make_config_widget("Diameter: ", self.diameter, self._on_diameter_value_changed)
        q_list_widget_items.append(diameter_widget)

        # thickness list element
        thickness_widget = self._make_config_widget("Thickness: ", self.thickness, self._on_thickness_value_changed)
        q_list_widget_items.append(thickness_widget)

        q_list_widget_items.append(self.surfaces[0].get_ui(1))
        q_list_widget_items.append(self.surfaces[1].get_ui(2))

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

    def clone(self):
        new_surface = self.surfaces[0].clone()
        new_surface2 = self.surfaces[1].clone()

        new_component = Lens(f"{self.component_name} copy",
                             self.y,
                             self.xr,
                             self.x,
                             self.thickness,
                             self.diameter,
                             self.refractive_index,
                             (new_surface, new_surface2))

        return new_component

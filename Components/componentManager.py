from Components.component import Component
from Components.lens import Lens, SurfaceProperties
from eventManager import signal_send, signal_subscribe


class ComponentManager:

    components:[Component] = []

    def new_component(self, component_type, component_name):
        if component_type == "Lens":
            new_part = Lens
            self.components.append(new_part)
            print(new_part.properties["part_name"])
            signal_send("components_changed", self.components)
        else:
            print("ComponentManager: Invalid component type")
            pass

    def get_list(self):
        return self.components


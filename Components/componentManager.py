from Components.component import Component
from Components.lens import Lens, SurfaceProperties

class ComponentManager:
    components:[Component] = []

    def newComponent(self, component_type, component_name):
        if component_type == "Lens":
            new_part = Lens(SurfaceProperties(), SurfaceProperties(), 30, 5)

        else:
            pass


    def getList(self):
        return self.components


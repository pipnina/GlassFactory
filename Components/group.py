from Components.component import Component, ComponentType


class Group(Component):
    def __init__(self,
                 component_name: str,
                 parent=None):

        if component_name is None:
            component_name = "New Group"

        super().__init__(component_name=component_name, component_type=ComponentType.Group, parent=parent, component_UUID=None)

        self.children: list[Component] = []

    def add_child(self, child: Component):
        for component in self.children:
            if component.component_UUID == child.component_UUID:
                print("Component already child of this group!")
                return

        if child.parent is not None:
            print("Component is already a child of another group!")
            return

        self.children.append(child)

    def remove_child(self, child: Component):
        for component in self.children:
            if component.component_UUID == child.component_UUID:
                component.parent = None
                self.children.remove(component)
                return


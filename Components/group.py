from Components.component import Component, ComponentType


class Group(Component):
    def __init__(self,
                 component_name: str,
                 ):

        if component_name is None:
            component_name = "New Group"

        super().__init__(component_name=component_name, component_type=ComponentType.Group)

        self.children: list[Component] = []

    def add_child(self, new_child: Component):
        if new_child not in self.children:
            self.children.append(new_child)
        else:
            print(f"Oh no! {new_child.component_name} is already owned by {self.component_name}!")

    def remove_child(self, old_child: Component):
        if old_child in self.children:
            self.children.remove(old_child)

    def duplicate(self):
        pass

from Components.component import Component, ComponentType


class Group(Component):
    def __init__(self,
                 component_name: str,
                 x=0,
                 y=0,
                 xr=0
                 ):

        if component_name is None:
            component_name = "New Group"

        super().__init__(component_name=component_name,
                         x=x,
                         y=y,
                         xr=xr)

        self.component_type = ComponentType.Group
        self.children: list[Component] = []

    def add_child(self, new_child: Component):
        if new_child not in self.children:
            self.children.append(new_child)
        else:
            print(f"Oh no! {new_child.component_name} is already owned by {self.component_name}!")

    def remove_child(self, old_child: Component):
        if old_child in self.children:
            self.children.remove(old_child)

    # We still duplicate the component as with other component classes, however
    # This function returns a list instead. So we need to handle it slightly differently.
    # because groups add themselves to the list returned by duplicate() first, we access it with [0] to set parent
    # other components are handled more simply
    def clone(self):
        new_component = Group(f"{self.component_name} copy",
                              self.x,
                              self.y,
                              self.xr)

        component_list = [new_component]

        for child in self.children:
            if type(child) is Group:
                new_child = child.clone()
                new_child[0].set_parent(new_component)
                component_list = component_list + new_child
            else:
                new_child = child.clone()
                new_child.set_parent(new_component)
                component_list.append(new_child)

        return component_list

from Components.component import Component, ComponentType
from Components.lens import Lens
from Components.group import Group
from event_manager import raise_event, Event


class ComponentManager:
    singleton_manager_instance = None

    def __init__(self):
        self.components: list[Component] = []
        self.copied_component: Component = None
        self.copied_component_has_been_cut: bool = False
        self.UUID_increment = 0

    @staticmethod
    def get_manager():
        if ComponentManager.singleton_manager_instance is None:
            ComponentManager.singleton_manager_instance = ComponentManager()
        return ComponentManager.singleton_manager_instance

    def new_component(self, component_type: ComponentType, component_name: str = None, parent: Component = None):
        new_component = None
        match component_type:
            case ComponentType.Lens:
                new_component = Lens(component_name=component_name)
            case ComponentType.Baffle:
                # TODO: Implement baffle
                exit("Baffle not implemented")
            case ComponentType.Prism:
                # TODO: Implement prism
                exit("Prism not implemented")
            case ComponentType.Camera:
                # TODO: Implement camera
                exit("Camera not implemented")
            case ComponentType.Focuser:
                # TODO: Implement focuser
                exit("Focuser not implemented")
            case ComponentType.Light:
                # TODO: Implement lights
                exit("Light not implemented")
            case ComponentType.Group:
                new_component = Group(component_name=component_name)
            case unknown_type:
                print(f"ComponentManager: Invalid component type: {unknown_type}")
                return

        self.UUID_increment += 1
        new_component.component_UUID = self.UUID_increment

        if parent is not None:
            new_component.set_parent(parent)

        self.components.append(new_component)
        raise_event(Event.ComponentChanged)

    def add_component_from_template(self, new_component: Component):
        self.UUID_increment += 1
        new_component.component_UUID = self.UUID_increment
        self.components.append(new_component)
        raise_event(Event.ComponentChanged)

    def add_components_from_list(self, new_components: list[Component]):
        for component in new_components:
            self.UUID_increment += 1
            component.component_UUID = self.UUID_increment
            self.components.append(component)
        raise_event(Event.ComponentChanged)

    @staticmethod
    def get_component_by_uuid(uuid: int):
        for component in ComponentManager.get_manager().components:
            if uuid != component.component_UUID:
                continue
            return component
        return None

    def cut_component(self, component: Component):
        self.copied_component = component
        self.copied_component_has_been_cut = True

    def copy_component(self, component: Component):
        self.copied_component = component
        self.copied_component_has_been_cut = False

    def paste_component(self, parent: Component):
        if self.copied_component is None:
            print("No item to paste")
            return

        if type(parent) is not Group and parent is not None:
            print("Must paste component into a group or tree root!")
            return

        if self.copied_component_has_been_cut:
            self.copied_component_has_been_cut = False
            self.copied_component.set_parent(parent)
            raise_event(Event.ComponentChanged)
            return

        if not self.copied_component_has_been_cut:
            new_components = self.copied_component.clone()
            if type(new_components) is list:
                new_components[0].set_parent(parent)
                self.add_components_from_list(new_components)
            else:
                new_components.set_parent(parent)
                self.add_component_from_template(new_components)

        """
        if not self.copied_component_has_been_cut:
            root_of_paste = self.new_component_by_copy(self.copied_component)
            self._duplicate_tree(root_of_paste, self.copied_component)
            root_of_paste.set_parent(parent)
            raise_event(Event.ComponentChanged)
            return
        """
    # We start with the root of the paste, with a new component by copy of the self.copied_component
    # We pass the copied_component and the root_of_paste to the _duplicate_tree method
    # The method checks if the "copied component" is a group or not. If not a group:
    # The method will return
    # If the "copied component" is a group:
    # The method will loop through the children of the root, create copies of them, and link them to the "copied comp"
    # The method will then call itself, with the "copied comp" being each of those children, and the "root" that of root
    """
    def _duplicate_tree(self, paste_root: Component, copied_comp: Component):
        if type(copied_comp) is Group:
            for component in copied_comp.children:
                new_child = self.new_component_by_copy(component)
                new_child.set_parent(paste_root)
                self._duplicate_tree(new_child, component)
        print("Is not a group: Skip!")
    """

    # This recursively removes a component from the component list, ensuring it takes its children with it!
    # Split into two functions to avoid having to call Event.ComponentChanged on every depth of the recursion
    def delete_component(self, component):
        self._delete_component_recurse(component)
        raise_event(Event.ComponentChanged)

    def _delete_component_recurse(self, component):
        if type(component) is Group:
            for child in component.children:
                self._delete_component_recurse(child)
        component.set_parent(None)
        self.components.remove(component)

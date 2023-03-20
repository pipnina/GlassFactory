from Components.component import Component, ComponentType
from Components.lens import Lens
from Components.group import Group
from event_manager import raise_event, Event
import copy


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

    def new_component_by_copy(self, referred: Component):
        component_type = referred.component_type
        match component_type:
            case ComponentType.Lens:
                new_component = Lens(referred.component_name)
                new_component.x = referred.x
                new_component.y = referred.y
                new_component.xr = referred.xr
                new_component.thickness = referred.thickness
                new_component.diameter = referred.diameter

                new_component.surfaces[0].is_flat = referred.surfaces[0].is_flat
                new_component.surfaces[0].is_reflective = referred.surfaces[0].is_reflective
                new_component.surfaces[0].focal_length = referred.surfaces[0].focal_length
                new_component.surfaces[0].conic_constant = referred.surfaces[0].conic_constant

                new_component.surfaces[1].is_flat = referred.surfaces[1].is_flat
                new_component.surfaces[1].is_reflective = referred.surfaces[1].is_reflective
                new_component.surfaces[1].focal_length = referred.surfaces[1].focal_length
                new_component.surfaces[1].conic_constant = referred.surfaces[1].conic_constant
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
                new_component = Group(referred.component_name)
                new_component.x = referred.x
                new_component.y = referred.y
                new_component.xr = referred.xr
            case unknown_type:
                print(f"ComponentManager: Invalid component type: {unknown_type}")
                return

        self.UUID_increment += 1
        new_component.component_UUID = self.UUID_increment

        # new_component.set_parent(referred.parent)

        self.components.append(new_component)
        raise_event(Event.ComponentChanged)
        return new_component

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
        # if type(parent) is not Group and type(parent) is not None:
        #    print("Not group not none")
        #    return

        if self.copied_component_has_been_cut:
            self.copied_component_has_been_cut = False
            self.copied_component.set_parent(parent)
            raise_event(Event.ComponentChanged)
            return

        if not self.copied_component_has_been_cut:
            root_of_paste = self.new_component_by_copy(self.copied_component)
            root_of_paste.set_parent(parent)
            self._duplicate_tree(root_of_paste, self.copied_component)
            raise_event(Event.ComponentChanged)
            return

    # We start with the root of the paste, with a new component by copy of the self.copied_component
    # We pass the copied_component and the root_of_paste to the _duplicate_tree method
    # The method checks if the "copied component" is a group or not. If not a group:
    # The method will return
    # If the "copied component" is a group:
    # The method will loop through the children of the root, create copies of them, and link them to the "copied comp"
    # The method will then call itself, with the "copied comp" being each of those children, and the "root" that of root

    def _duplicate_tree(self, paste_root: Component, copied_comp: Component):
        if type(copied_comp) is Group:
            for component in copied_comp.children:
                new_child = self.new_component_by_copy(component)
                new_child.set_parent(paste_root)
                self._duplicate_tree(new_child, component)

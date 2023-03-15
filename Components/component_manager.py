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

    def new_component_by_reference(self, referred: Component):
        component_type = type(referred)
        match component_type:
            case ComponentType.Lens:
                new_component = Lens(referred.component_name)
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
            case unknown_type:
                print(f"ComponentManager: Invalid component type: {unknown_type}")
                return

        self.UUID_increment += 1
        new_component.component_UUID = self.UUID_increment

        if referred.parent is not None:
            new_component.set_parent(referred.parent)

        self.components.append(new_component)
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
        if type(parent) is not Group and type(parent) is not None:
            return

        if self.copied_component_has_been_cut:
            self.copied_component_has_been_cut = False
            self.copied_component.set_parent(parent)
            raise_event(Event.ComponentChanged)
            return

        new_component = copy.deepcopy(self.copied_component)
        new_component.set_parent(None)
        new_component.set_parent(parent)
        if type(new_component) is Group:
            for child in new_component.children:

                child.set_parent(new_component)
        self.components.append(new_component)
        # self.copied_component.set_parent(parent)
        # self.components.append(self.copied_component)
        raise_event(Event.ComponentChanged)

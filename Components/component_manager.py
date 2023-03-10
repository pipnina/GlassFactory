from Components.component import Component, ComponentType
from Components.lens import Lens
from Components.group import Group
from event_manager import raise_event, Event


class ComponentManager:
    singleton_manager_instance = None

    def __init__(self):
        self.components: list[Component] = []
        self.selected_component: int
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

        print(f"Part parent: {new_component.parent}")

        self.components.append(new_component)
        raise_event(Event.ComponentChanged)

    @staticmethod
    def get_component_by_uuid(uuid: int):
        for component in ComponentManager.get_manager().components:
            if uuid != component.component_UUID:
                continue
            return component
        return None

from Components.component import Component, ComponentType
from Components.lens import Lens
from event_manager import raise_event, Event


class ComponentManager:
    singleton_manager_instance = None

    def __init__(self):
        self.components: list[Component] = []
        self.UUID_increment = 0

    @staticmethod
    def get_manager():
        if ComponentManager.singleton_manager_instance is None:
            ComponentManager.singleton_manager_instance = ComponentManager()
        return ComponentManager.singleton_manager_instance

    def new_component(self, component_type: ComponentType, component_name: str = None):
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
                # TODO: Implement groups
                exit("Group not implemented")
            case unknown_type:
                print(f"ComponentManager: Invalid component type: {unknown_type}")
                return
        new_component.component_UUID = self.choose_UUID()

        self.components.append(new_component)
        raise_event(Event.ComponentChanged)

    def choose_UUID(self):
        self.UUID_increment += 1
        return self.UUID_increment

from PySide6.QtWidgets import QMenuBar

from Components.component import ComponentType
from Components.component_manager import ComponentManager


class MenuBar(QMenuBar):

    parts_manager = [ComponentManager]

    def __init__(self):
        super().__init__()
        # Create the interactions for the "file" menu
        file_menu = self.addMenu("File")
        #Create the interaction for the "New" submenu
        file_menu_new = file_menu.addMenu("New")
        new_menu_group = file_menu_new.addAction("Group")
        new_menu_lens = file_menu_new.addAction("Lens")


        new_menu_lens.triggered.connect(lambda: self.file_add_clicked(ComponentType.Lens))
        new_menu_group.triggered.connect(lambda: self.file_add_clicked(ComponentType.Group))



        file_menu_open = file_menu.addAction("Open")
        file_menu_open_recent = file_menu.addMenu("Open recent:")

        self.addMenu("Edit")
        self.addMenu("Generate")


    @staticmethod
    def file_add_clicked(part_type: ComponentType):
        ComponentManager.get_manager().new_component(part_type)
        print("Been pressed")

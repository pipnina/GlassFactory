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
        file_menu_new = file_menu.addAction("New")
        file_menu_new.triggered.connect(self.file_add_clicked)


        file_menu_open = file_menu.addAction("Open")
        file_menu_open_recent = file_menu.addMenu("Open recent:")

        self.addMenu("Edit")
        self.addMenu("Generate")


    @staticmethod
    def file_add_clicked():
        ComponentManager.get_manager().new_component(component_type=ComponentType.Lens)
        print("Been pressed")

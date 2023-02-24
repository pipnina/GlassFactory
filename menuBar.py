from PySide6.QtWidgets import QMenuBar
from Components.componentManager import ComponentManager


class MenuBar(QMenuBar):

    parts_manager = [ComponentManager]

    def __init__(self, parts_manager: ComponentManager):
        super().__init__()
        self.parts_manager = parts_manager

        # Create the interactions for the "file" menu
        file_menu = self.addMenu("File")
        #Create the interaction for the "New" submenu
        file_menu_new = file_menu.addAction("New")
        # file_menu_new.clicked.connect(self.fileAddClicked())
        file_menu_new.triggered.connect(self.file_add_clicked)


        file_menu_open = file_menu.addAction("Open")
        file_menu_open_recent = file_menu.addMenu("Open recent:")

        self.addMenu("Edit")
        self.addMenu("Generate")


    def file_add_clicked(self):
        self.parts_manager.new_component("Lens", "New Lens")
        print("Been pressed")

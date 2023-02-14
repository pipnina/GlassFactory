from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()
        file_menu = self.addMenu("File")
        file_menu_new = file_menu.addAction("New")
        file_menu_open = file_menu.addAction("Open")
        file_menu_open_recent = file_menu.addMenu("Open recent:")

        self.addMenu("Edit")
        self.addMenu("Generate")
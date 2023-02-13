from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()
        fileMenu = self.addMenu("File")
        fileMenuNew = fileMenu.addAction("New")
        fileMenuOpen = fileMenu.addAction("Open")
        fileMenuOpenRecent = fileMenu.addMenu("Open recent:")

        self.addMenu("Edit")
        self.addMenu("Generate")
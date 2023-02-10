import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

app = QApplication(sys.argv)

class MainWindow(QWidget):
    menuBar = QMenuBar()
    treeView = QTreeView()
    verticalLayout = QVBoxLayout() #contains a horizontal layout for joining the menu bar, tree/edit and 3d view

    def __init__(self):
        self.build_menu_bar()
        self.build_tree_view()
        self.build_edit_view()
        self.build_3d_view()
        self.build_layout()

    def build_menu_bar(self):
        fileMenu = self.menuBar.addMenu("File")
        fileMenuNew = fileMenu.addAction("New")
        fileMenuOpen = fileMenu.addAction("Open")
        fileMenuOpenRecent = fileMenu.addMenu("Open recent:")

        self.menuBar.addMenu("Edit")
        self.menuBar.addMenu("Generate")
        #self.menuBar.show()

    def build_tree_view(self):
        #self.treeView.show()
        pass

    def build_edit_view(self):
        pass

    def build_3d_view(self):
        pass

    def build_layout(self):
        #self.verticalLayout.addWidget(self.menuBar)
        #self.verticalLayout.addWidget(self.treeView)
        self.menuBar.setLayout(self.verticalLayout)
        self.treeView.setLayout(self.verticalLayout)



def main():
    app.setApplicationDisplayName("GlassFactory")
    main_window = MainWindow()
    app.exec()


if __name__ == '__main__':
    main()

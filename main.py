import sys
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QListView, QGraphicsView, QVBoxLayout, QHBoxLayout
from menuBar import MenuBar

app = QApplication(sys.argv)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.menuBar = MenuBar()
        self.treeView = QTreeView(self)
        self.listView = QListView(self)
        self.graphicsViewport = QGraphicsView(self)
        self.verticalLayout_MenuMerger = QVBoxLayout(self)  # contains a horizontal layout for joining the menu bar, to the layout containing the rest of the window
        self.verticalLayout_TreeMerger = QVBoxLayout(self) # contains the two trees above and below eachother
        self.horizontalLayout_Tree3DMerger = QHBoxLayout(self) # Joins the trees and the 3D space together

        self.build_layout()

    def build_layout(self):
        self.verticalLayout_MenuMerger.addWidget(self.menuBar)
        self.verticalLayout_MenuMerger.addLayout(self.horizontalLayout_Tree3DMerger)

        self.horizontalLayout_Tree3DMerger.addLayout(self.verticalLayout_TreeMerger)
        self.horizontalLayout_Tree3DMerger.addWidget(self.graphicsViewport)

        self.verticalLayout_TreeMerger.addWidget(self.treeView)
        self.verticalLayout_TreeMerger.addWidget(self.listView)

        self.show()
        pass


def main():
    app.setApplicationDisplayName("GlassFactory")
    main_window = MainWindow()
    app.exec()


if __name__ == '__main__':
    main()

import sys
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QListView, QGraphicsView, QVBoxLayout, QHBoxLayout
from menu_bar import MenuBar
from editor_panel import EditorPanel
from graphics_viewport import GraphicsViewport

app = QApplication(sys.argv)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Build the UI elements
        self.menu_bar = MenuBar()
        self.editor_panel = EditorPanel()
        self.graphics_viewport = GraphicsViewport()

        self.verticalLayout_MenuMerger = QVBoxLayout(
            self)  # contains a horizontal layout for joining the menu bar, to the layout containing the rest of the window
        self.verticalLayout_TreeMerger = QVBoxLayout(self)  # contains the two trees above and below eachother
        self.horizontalLayout_Tree3DMerger = QHBoxLayout(self)  # Joins the trees and the 3D space together

        self.build_layout()

        # Now we link them together as needed

    # Combine UI elements into a layout to present them properly on screen
    def build_layout(self):
        self.verticalLayout_MenuMerger.addWidget(self.menu_bar)
        self.verticalLayout_MenuMerger.addLayout(self.horizontalLayout_Tree3DMerger)

        self.horizontalLayout_Tree3DMerger.addLayout(self.editor_panel)
        self.horizontalLayout_Tree3DMerger.addWidget(self.graphics_viewport)

        self.show()


def main():
    app.setApplicationDisplayName("GlassFactory")
    main_window = MainWindow()
    app.exec()


if __name__ == '__main__':
    main()

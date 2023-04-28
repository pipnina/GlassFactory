import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QMainWindow
from UI_code.menu_bar import MenuBar
from UI_code.editor_panel import EditorPanel
from UI_code.graphics_viewport import GraphicsViewport

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 900)
        # Build the UI elements
        self.menu_bar = MenuBar()
        self.editor_panel = EditorPanel()
        self.graphics_viewport = GraphicsViewport()

        # Joins the trees and the 3D space together
        self.menu_viewport_splitter = QSplitter(self)
        self.menu_viewport_splitter.addWidget(self.editor_panel)
        self.menu_viewport_splitter.addWidget(self.graphics_viewport)

        self.setCentralWidget(self.menu_viewport_splitter)
        self.setMenuBar(self.menu_bar)
        self.show()


def main():
    app.setApplicationDisplayName("GlassFactory")
    main_window = MainWindow()
    app.exec()


if __name__ == '__main__':
    main()

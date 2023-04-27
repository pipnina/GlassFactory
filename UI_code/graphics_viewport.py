from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem
from PySide6.QtCore import QRectF
from PySide6.QtGui import QTransform


class GraphicsViewport(QGraphicsView):

    def __init__(self):
        super().__init__()

        scene = QGraphicsScene()
        test_rect = scene.addRect(QRectF(0, 0, 100, 100))

        item = scene.itemAt(50, 50, QTransform())
        self.setScene(scene)

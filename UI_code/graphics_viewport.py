from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsPolygonItem
from PySide6.QtCore import QRectF, QPointF
from PySide6.QtGui import QTransform, QPolygonF, QPolygon
import math


class GraphicsViewport(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.points_per_mm = 1
        self.setMinimumWidth(800)

        scene = self.build_overview_scene()
        self.setScene(scene)


    def build_overview_scene(self):
        scene = QGraphicsScene()
        points = [QPointF(500,500),QPointF(70,20),QPointF(40,80),QPointF(60,120),QPointF(80,160), QPointF(100, 200), QPointF(120, 240)]
        test_rect = scene.addPolygon(QPolygonF(points, closed=False))

        polygon = QPolygonF([QPointF(0.0,0.0), QPointF(30.0, 0.0), QPointF(15.0,40.0), QPointF(15.0, 80.0), QPointF(0.0, 80.0)])
        polygon_item = QGraphicsPolygonItem(polygon)
        scene.addItem(polygon_item)

        curve_polygon_points = self.build_conic_curve(300, -1, 100)
        curve_polygon_item = QGraphicsPolygonItem(curve_polygon_points)
        scene.addItem(curve_polygon_item)
        print(curve_polygon_points)


        return scene

    # Generate a conic curve from parameters, and return the points sweeping from one edge to another on the radial axis
    # x = SQRT(y-squared / R + SQRT(R-squared - (K-1) * y-squared))
    # In this case, the apex of the curve is at the origin, and is tangential to the Y axis.
    # This means we know the Y position, and simply want to calculate x for each y position.
    def build_conic_curve(self, focal_length, conic_constant, radius):
        pointcloud: QPointF = []

        #create the samples for one side, then add the middle, and append the first side in reverse
        num_of_points = radius * self.points_per_mm
        increment = radius / num_of_points

        for point in range(num_of_points, 1):
            y = point * increment
            x = math.sqrt(y*y / radius+math.sqrt(radius*radius - (conic_constant-1) * y*y))
            pointcloud.append(QPointF(x, y))

        return pointcloud

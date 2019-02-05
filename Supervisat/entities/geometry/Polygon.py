from typing import List

from entities.geometry import Point2D, Shape


class Polygon(Shape):
    def __init__(self, points: List[Point2D]):
        super(Polygon, self).__init__()
        self._points = []
        for p in points:
            self._points.append(Point2D(round(p.x, 2), round(p.y, 2)))

    @property
    def points(self) -> List[Point2D]:
        return self._points
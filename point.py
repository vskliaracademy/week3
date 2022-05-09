class Point2D():
    _points_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D._points_count += 1

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    @property
    def points_count(self):
        return Point2D._points_count


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 +
                (self.z - point.z) ** 2) ** 0.5


if __name__ == "__main__":
    p1 = Point2D(10, 20)
    p2 = Point2D(10, 50)
    p3 = Point2D(20, 30)

    p4 = Point3D(10, 20, 30)
    p5 = Point3D(10, 50, 30)
    p6 = Point3D(20, 30, 40)

    dist = p1.distance(p2)
    print(dist)
    print(Point2D.points_count)
    print(p3.points_count)
    print()
    dist2 = p6.distance(p5)
    print(dist2)

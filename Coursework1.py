import random
import math
from itertools import combinations
from collections import defaultdict

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class UniquePointGenerator:
    def __init__(self, count: int, x_range=(-10, 10), y_range=(-10, 10)):
        self.count = count
        self.x_range = x_range
        self.y_range = y_range

    def generate_points(self):
        points_set = set()
        while len(points_set) < self.count:
            x = random.randint(*self.x_range)
            y = random.randint(*self.y_range)
            points_set.add((x, y))
        return [Point(x, y) for x, y in points_set]


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f"Triangle: {self.p1}, {self.p2}, {self.p3}"

    def perimeter(self) -> float:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        return a + b + c

    def area(self) -> float:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(max(0, s * (s - a) * (s - b) * (s - c)))

    def triangle_type(self) -> str:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        if abs(a - b) < 0.001 and abs(b - c) < 0.001:
            return "Рівносторонній"
        elif abs(a - b) < 0.001 or abs(b - c) < 0.001 or abs(a - c) < 0.001:
            return "Рівнобедрений"
        else:
            return "Довільний"


class TriangleData:
    def __init__(self, points: list[Point]):
        self.points = points
        self.triangles = self._generate_triangles()

    def _are_not_colinear(self, a: Point, b: Point, c: Point) -> bool:
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) != 0

    def _generate_triangles(self):
        triangles = []
        for p1, p2, p3 in combinations(self.points, 3):
            if self._are_not_colinear(p1, p2, p3):
                triangles.append(Triangle(p1, p2, p3))
        return triangles

    def count_triangles(self) -> int:
        return len(self.triangles)

    def get_largest_triangle(self) -> Triangle:
        return max(self.triangles, key=lambda t: t.area(), default=None)

    def get_smallest_triangle(self) -> Triangle:
        return min(self.triangles, key=lambda t: t.area(), default=None)

    def get_triangles_by_type(self) -> dict:
        type_counts = defaultdict(int)
        for triangle in self.triangles:
            t_type = triangle.triangle_type()
            type_counts[t_type] += 1
        return dict(type_counts)
generator = UniquePointGenerator(20)
points = generator.generate_points()
analyzer = TriangleData(points)
print(f"Згенеровано точок: {len(points)}")
print(f"Кількість можливих трикутників: {analyzer.count_triangles()}")

largest = analyzer.get_largest_triangle()
if largest:
    print("\nНайбільший трикутник:")
    print(largest)
    print("Площа:", largest.area())
    print("Периметр:", largest.perimeter())

smallest = analyzer.get_smallest_triangle()
if smallest:
    print("\nНайменший трикутник:")
    print(smallest)
    print("Площа:", smallest.area())
    print("Периметр:", smallest.perimeter())
print("\nСтатистика за типами трикутників:")
types = analyzer.get_triangles_by_type()
for ttype, count in types.items():
    print(f"{ttype}: {count}")
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def Area(self):
        return 0  # 点没有面积

class Rectangle(Point):
    def __init__(self, x=0, y=0, width=0, height=0):
        super().__init__(x, y)  # 调用父类构造函数
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle at ({self.x}, {self.y}) with width={self.width}, height={self.height}"

    def Area(self):
        return self.width * self.height

class Circle(Point):
    def __init__(self, x=0, y=0, radius=0):
        super().__init__(x, y)  # 调用父类构造函数
        self.radius = radius

    def __str__(self):
        return f"Circle at ({self.x}, {self.y}) with radius={self.radius}"

    def Area(self):
        return math.pi * self.radius * self.radius

# 测试代码
if __name__ == "__main__":
    # 创建Point对象
    point = Point(1, 1)
    print(f"{point} - Area: {point.Area()}")

    # 创建Rectangle对象
    rect = Rectangle(0, 0, 5, 3)
    print(f"{rect} - Area: {rect.Area()}")

    # 创建Circle对象
    circle = Circle(2, 2, 4)
    print(f"{circle} - Area: {circle.Area():.2f}")

    # 创建一个包含不同形状的列表并计算它们的面积
    shapes = [
        Point(0, 0),
        Rectangle(1, 1, 4, 6),
        Circle(2, 2, 3)
    ]

    print("\n计算所有形状的面积：")
    for shape in shapes:
        print(f"{shape.__class__.__name__}的面积: {shape.Area():.2f}")
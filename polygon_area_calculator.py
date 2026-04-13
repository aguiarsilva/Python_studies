import math

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for line in range(self.height):
            picture += ("*" * self.width) + "\n"
        return picture

    def get_amount_inside(self, shape) -> int:
        if not isinstance(shape, Rectangle):
            raise ValueError("The passed-in shape must be a rectangle or a square.")

        amount_inside = (self.height // shape.height) * (self.width // shape.width)
        return amount_inside

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.side = side

    def set_width(self, side: float) -> None:
        self.width = side
        self.height = side
        self.side = side
    
    def set_height(self, side: float) -> None:
        self.height = side
        self.width = side
        self.side = side
    
    def set_side(self, side: float) -> None:
        self.height = side
        self.width = side
        self.side = side
    
    def __str__(self) -> str:
        return f"Square(side={self.side})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

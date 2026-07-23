from dataclasses import dataclass


# ---------------- Parent Class ----------------
class Rectangle:
    def __init__(self, height, width):
        print("Rectangle __init__ called")

        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


# ---------------- Child Class ----------------
@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        print("Square __post_init__ called")

        # Call the parent constructor
        super().__init__(self.side, self.side)


# ---------------- Main Program ----------------
sq = Square(5)

print("\nObject:")
print(sq)

print("\nAttributes")
print("Side   :", sq.side)
print("Height :", sq.height)
print("Width  :", sq.width)

print("\nArea :", sq.area())               
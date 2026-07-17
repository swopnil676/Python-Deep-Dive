class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # getter
    def radius(self):
        """Get the radius of the circle."""
        return self._radius

    @radius.setter # setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius.deleter
    def radius(self):
        print("deleted")
        del self._radius

    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self._radius * 2

# Usage
c = Circle(5)
del c.radius
# print(c.radius)    # 5
# print(c.diameter)  # 10
# c.radius = -10
# print(c.radius)    # 10
# print(c.diameter)  # 20
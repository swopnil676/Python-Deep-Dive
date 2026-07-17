class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other):
        if not isinstance(other, Product):
            # don't attempt to compare against unrelated types
            return NotImplemented
        
        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )

# ------------------ Usage ------------------

p1 = Product("Laptop", 50000, 2)
p2 = Product("Laptop", 50000, 2)
p3 = Product("Mouse", 500, 5)

# Object representation
print(p1)
# Product(name='Laptop', price=50000, quantity=2)

# Total cost
print("Total cost of p1:", p1.total_cost())
# 100000

print("Total cost of p3:", p3.total_cost())
# 2500

# Equality comparison
print("p1 == p2:", p1 == p2)  # True
print("p1 == p3:", p1 == p3)  # False

# Comparison with another type
print("p1 == 100:", p1 == 100)  # False
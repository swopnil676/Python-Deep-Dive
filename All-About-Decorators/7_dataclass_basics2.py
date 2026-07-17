from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

# Creating object instances
p1 = Product(name="Laptop", price=1000.0, quantity=3)
p2 = Product(name="Laptop", price=1000.0, quantity=3)
p3 = Product(name="Smartphone", price=500.0, quantity=2)

# Testing the functionality
print(p1)               # Output: Product(name='Laptop', price=1000.0, quantity=3)
print(p1.total_cost())  # Output: 3000.0
print(p1 == p2)         # Output: True
print(p1 == p3)         # Output: False
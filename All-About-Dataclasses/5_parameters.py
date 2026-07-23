from dataclasses import dataclass, field

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    sizes: list[str] = field(default_factory=list)


    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


I1 = InventoryItem("Shirt", 500, 2)
I2 = InventoryItem("Shoes", 1200, 1)

I1.sizes.append("M")
I2.sizes.append("42")

print(I1)
print(I2)
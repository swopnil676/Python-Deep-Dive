from dataclasses import dataclass
from typing import ClassVar

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    
    tax_rate: ClassVar[int] = 100


item = InventoryItem("Laptop", 50000)

print(item)
print(item.tax_rate)
print(InventoryItem.tax_rate)
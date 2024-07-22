class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f} each"








class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def get_total_value(self):
        return sum(item.quantity * item.price for item in self.items)

    def __str__(self):
        inventory_str = '\n'.join(str(item) for item in self.items)
        return f"Inventory:\n{inventory_str}\nTotal value: ${self.get_total_value():.2f}"











# Create an inventory
inventory = Inventory()

# Add items to the inventory
inventory.add_item(Item("Apple", 50, 0.5))
inventory.add_item(Item("Banana", 100, 0.3))
inventory.add_item(Item("Orange", 75, 0.8))

# Update item quantity and price
inventory.items[0].update_quantity(25)
inventory.items[1].update_price(0.35)

# Remove an item
inventory.remove_item("Orange")

# Print the inventory
print(inventory)

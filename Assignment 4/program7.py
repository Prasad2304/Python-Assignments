  # Inventory Management System

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

# Add a new product
def add_product(name, quantity):
    inventory[name] = quantity
    print(name, "added successfully.")

# Update product quantity
def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(name, "quantity updated.")
    else:
        print("Product not found.")

# Remove product if quantity is 0
def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]
        print(name, "removed from inventory.")
    else:
        print("Product cannot be removed.")

# Display product with highest stock
def highest_stock():
    product = max(inventory, key=inventory.get)
    print("Highest stock:", product, "=", inventory[product])

# Display total unique products
def total_products():
    print("Total unique products:", len(inventory))


# Function calls
add_product("Mobile", 20)
update_product("Mouse", 30)
highest_stock()
total_products()

inventory["Keyboard"] = 0
remove_product("Keyboard")

print("Final Inventory:", inventory)
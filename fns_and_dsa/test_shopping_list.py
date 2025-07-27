from shopping_list_manager import add_item, remove_item, view_list



# Initialize an empty list
shopping_list = []

print("🛒 Adding milk...")
add_item("milk", shopping_list)

print("🛒 Adding bread...")
add_item("bread", shopping_list)

print("📋 Viewing list:")
view_list(shopping_list)

print("🗑️ Removing milk...")
remove_item("milk", shopping_list)

print("✅ Final list:")
view_list(shopping_list)

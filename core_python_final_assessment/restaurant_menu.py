def add_item(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} is already on the menu.")
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not on the menu.")
    return menu

def check_item(menu, item):
    if item in menu:
        return f"{item} is available."

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item_to = "Tacos"
remove_item_to = "Salad"
check_item_to = "Pizza"
updated_menu = add_item(initial_menu, add_item_to)
updated_menu = remove_item(updated_menu, remove_item_to)
availability = check_item(updated_menu, check_item_to)
print("\nUpdated menu:", updated_menu)
print("Availability:", availability)

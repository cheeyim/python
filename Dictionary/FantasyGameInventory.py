def display_inventory(inventory):
    total_count = 0
    print("Inventory:")
    for k, v in inventory.items():
        print("{0} {1}".format(v, k))
        total_count += v
    print("Total number of items: " + str(total_count))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(stuff, dragonLoot)
display_inventory(inv)
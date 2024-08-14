# First part (Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + str(k) + '(s)')
    print('Total number of items: ' + str(item_total))
    print('')

displayInventory(stuff)

# Second part (List to Dictionary Function for Fantasy Game Inventory)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

print('You\'ve defeated a dragon and its loot has been transferred to your inventory' + '\n')

displayInventory(addToInventory(stuff, dragonLoot))

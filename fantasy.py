things = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
  print("Inventory: ")
  item_total = 0
  
  for name, items in inventory.items():
        print(f'{name:<10} : {items:>2}')
        item_total += items
  print(f'Total number of items is {item_total}') 







display_inventory(things)
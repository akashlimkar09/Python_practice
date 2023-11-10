def update_inventory(arr1, arr2):
    
    combined_arr = arr1 + arr2

    inventory_dict = {}

    # Populate the dictionary with quantities
    for item in combined_arr:
        quantity = inventory_dict.get(item[1], 0)
        inventory_dict[item[1]] = quantity + item[0]

    # dictionary to list
    new_inventory = [[quantity, item] for item, quantity in inventory_dict.items() if quantity != 0]

    # Sort
    new_inventory.sort(key=lambda x: x[1])

    return new_inventory

cur_inv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

new_inv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

print(update_inventory(cur_inv, new_inv))

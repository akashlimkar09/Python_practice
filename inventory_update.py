def update_inventory(arr1, arr2):
    # Combine the arrays
    combined_arr = arr1 + arr2

    # Use a regular dictionary to accumulate quantities by item name
    #item_counts = {}
    #for quantity, item in combined_arr:
    #   item_counts[item] = item_counts.get(item, 0) + quantity
        
    item_counts = {}
    for quantity, item in combined_arr:
        if item in item_counts:
            item_counts[item] = item_counts[item] + quantity
        else:
            item_counts[item] = quantity

    # Convert dictionary items to a list of lists
    #new_inventory = []
    #for item, quantity in item_counts.items():
    #    if quantity != 0:
    #        new_inventory.append([quantity, item])
            
    new_inventory = []
    for item in item_counts:
        quantity = item_counts[item]
        if quantity != 0:
            new_inventory.append([quantity, item])

    # Sort the list based on item names
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

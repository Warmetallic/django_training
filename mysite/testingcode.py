
def test(text):
    result = text.split("ness")[0]

    if(result.endswith("i")):
        return result[:-1] + 'y'
    else:
        return result


print(test("heaviness"))




def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    items_dic = {}
    i = 0
    for item in items:
        i += 1
        items_dic[item] = i
        
    return items_dic

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(create_inventory(list1))


def create_inventory2(items):
    items_dic = {}
    for item in items:
        if item in items_dic:
            items_dic[item] += 1
        else:
            items_dic[item] = 1

        
    return items_dic

list1 = ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'h', 'i', 'j']

print(create_inventory2(list1))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            
    return inventory

print(decrement_items(create_inventory2(list1), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
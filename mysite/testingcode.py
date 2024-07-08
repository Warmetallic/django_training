from functools import reduce


def test(text):
    result = text.split("ness")[0]

    if result.endswith("i"):
        return result[:-1] + "y"
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


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(create_inventory(list1))


def create_inventory2(items):
    items_dic = {}
    for item in items:
        if item in items_dic:
            items_dic[item] += 1
        else:
            items_dic[item] = 1

    return items_dic


list1 = ["a", "a", "c", "d", "d", "d", "g", "h", "i", "j"]

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


print(
    decrement_items(
        create_inventory2(list1), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    )
)

from functools import wraps


def multiply_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) * 2
        return result

    return wrapper


def say_hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)

    return wrapper


@say_hello
@multiply_decorator
def find_even(numbers: list) -> int:
    result = 0
    for number in numbers:
        result += number % 2 == 0
    return result


number_even = [1, 2, 34, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(find_even(number_even))


def print_special_numbers():
    for number in range(0, 1001):
        if number % 3 == 0 and number % 5 != 0:
            if sum(int(digit) for digit in str(number)) < 10:
                print(number)


print_special_numbers()


list_forlambda = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0 and x > 4, list_forlambda))

print(result)


values = [(1, "hello", 3), (2, "bye", 4), (3, "aba", 0)]

result2 = sorted(values, key=lambda x: x[0] + x[2])

print(result2)


result3 = reduce(lambda acc, x: acc + x, list_forlambda)
print(result3)


max_value = reduce(lambda acc, x: acc if acc > x else x, list_forlambda)
print(max_value)


class Person:
    def __new__(cls, name, age):
        # This method is called before __init__, and it must return an instance of the class.
        # Here, we're not doing anything special, just calling the superclass's __new__ method.
        instance = super(Person, cls).__new__(cls)
        # You could add custom logic here before the instance is created.
        return instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


test_person = Person("John", 30)
print(test_person)

from functools import wraps
import random

test_list = [1, 2, 3, 4, 5, 6]


def length_function(list: list):
    result = []
    for element in list:
        if (element % 2) == 0:
            result.append(element)
    return result


print(length_function(test_list))


def invert(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result = list(map(lambda x: -x, result))
        else:
            raise RuntimeError()
        return result

    return wrapper


@invert
def length_function2(length: int = 10):
    if length == 0:
        return 0
    is_negative = length < 0
    # result = []
    # for element in range(abs(length)):
    #     if (element % 2) == 0:
    #         result.append(element if not is_negative else -element)
    return [i if not is_negative else -i for i in range(abs(length)) if i % 2 == 0]


print(length_function2(10))


# def test():
#     assert length_function2(10) == [0, 2, 4, 6, 8]
#     assert length_function2(-4) == [0, -2]
#     assert length_function2(0) == [0]


# test()
def reverse_func(array_list: list) -> list:
    result = array_list.reverse()
    return array_list


def reverse_func2(array_list: list) -> list:
    result = []
    list_length = len(array_list)
    for i in range(list_length):
        result.append(array_list[list_length - i - 1])
    return result


def reverse_func3(array_list: list) -> list:
    return array_list[::-1]


print(reverse_func3(test_list))


def get_first_matching_object(predicate, objects=[]):
    for obj in objects:
        if predicate(obj):
            return obj
    return None


cat = "cat"
animals = [cat, "dog"]

print(get_first_matching_object(lambda x: x == cat, animals))


# def decorator(exceptions: list[tuple[Exception, callable[[], None]]]):
#     def wrapper(func):
#         @wraps(tuple)
#         def wrapper1(*args, **kwargs):
#             try:
#                 res = func(*args, **kwargs)
#             except Exception as e:
#                 for ex in exceptions:
#                     if isinstance(e, ex[0]):
#                         ex[1]()
#                         raise e
#             return res

#         return wrapper1

#     return wrapper


# def bar():
#     print("1")


# @decorator([(KeyError, bar), (IndexError, lambda _: print(2))])
# def foo():
#     if random.randint(1, 2) == 1:
#         raise KeyError("bar")
#     else:
#         raise IndexError


class Stack:
    def __init__(self, array_list: list[int] = [-22, -111, 2, 3, -400]):
        self.array_list = array_list

    def add_number(self, number: int):
        if isinstance(number, int):
            self.array_list.append(number)
        else:
            raise TypeError

    def pop_number(self):
        self.array_list.pop()

    def top(self):
        return self.array_list[-1]

    def find_min(self):
        # min = self.array_list[0]
        # for number in self.array_list:
        #     if number < min:
        #         min = number
        return min(self.array_list)


new_class = Stack()
new_class.add_number(1)
new_class.pop_number()
new_class.find_min()

print(new_class.find_min())


test2 = "hello there"

test3 = test2.split(" ")

test4 = " ".join(test3)


print((test4))

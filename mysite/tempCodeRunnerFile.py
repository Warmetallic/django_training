from functools import cache


@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print("Hello, World!")
    print(factorial(5))


if __name__ == "__main__":
    main()

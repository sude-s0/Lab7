def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y==0:
        return 'Divider can not be 0!'
    else:
        return x/y

def power(x, y):
    return x**y


def mod(x, y):
    if y == 0:
        return 'Cannot be modded by 0!'
    return x % y

if __name__ == "__main__":
    print("Testing: ")
    print("5 + 2 =", add(5, 2))
    print("10 - 3 =", subtract(10, 3))
    print("4 * 6 =", multiply(4, 6))
    print("8 / 0 =", divide(8, 0))
    print("3 ** 4 =", power(3, 4))
    print("10 % 0 =", mod(10, 0))


from adder import adder


def multiplier(a: int, b: int) -> int:
    result = 0
    while b > 0:
        if b & 1:
            result = adder(result, a)
        a = a << 1
        b = b >> 1
    return result


def main():
    print(multiplier(4, 3))
    print(multiplier(6, 7))


if __name__ == "__main__":
    main()

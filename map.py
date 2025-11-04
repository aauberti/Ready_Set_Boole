def map(x: int, y: int) -> int | None:
    if not (0 <= x <= 65535 and 0 <= y <= 65535):
        print("Error: values must be between 0 and 65535")
        return None

    x = x & 0xFFFF
    y = y & 0xFFFF
    res = 0
    for i in range(16):
        res |= ((x >> i) & 1) << (2 * i + 1)
        res |= ((y >> i) & 1) << (2 * i)

    return res / (2**32 - 1)


def main():
    print(map(0, 0))
    print("-----")
    print(map(65535, 65535))
    print("-----")
    print(map(8, 3))


if __name__ == "__main__":
    main()

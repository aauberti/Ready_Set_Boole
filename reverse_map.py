from map import map


def reverse_map(n: float) -> tuple[int, int] | None:
    if not (0 <= n <= 1):
        print("Error: value must be between 0 and 1")
        return None

    res = int(n * 0xFFFFFFFF)
    x = 0
    y = 0
    for i in range(16):
        y |= ((res >> (2 * i)) & 1) << i
        x |= ((res >> (2 * i + 1)) & 1) << i

    return x, y


def main():
    print(reverse_map(map(0, 0)))
    print("-----")
    print(reverse_map(map(65535, 65535)))
    print("-----")
    print(reverse_map(map(42, 42)))
    print("-----")


if __name__ == "__main__":
    main()

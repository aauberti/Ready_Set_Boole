def reverse_map(n: int) -> tuple[int, int] | None:
    if not (0 <= n < 2**16):
        print("Error")
        return None

    x = 0
    y = 0
    i = n
    step = 1
    while step < 256:
        quadrant_x = 1 & (i // 2)
        quadrant_y = 1 & (i ^ quadrant_x)

        if quadrant_y == 0:
            if quadrant_x == 1:
                x, y = step - 1 - x, step - 1 - y
            x, y = y, x

        x += step * quadrant_x
        y += step * quadrant_y

        i //= 4
        step *= 2

    return x, y


def main():
    print(reverse_map(0))
    print("-----")
    print(reverse_map(65535))
    print("-----")
    print(reverse_map(4))
    print("-----")


if __name__ == "__main__":
    main()

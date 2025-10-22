def adder(a: int, b: int) -> int:
    while b != 0:
        S = a ^ b
        R = (a & b) << 1

        a = S
        b = R
    return a

def main():
    print(adder(4, 5))
    print(adder(10, 50))


if __name__ == "__main__":
    main()
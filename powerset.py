def powerset(set: list) -> list:
    result = [[]]

    for element in set:
        result.extend([subset + [element] for subset in result])

    return result


def main():
    print(powerset([0, 1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

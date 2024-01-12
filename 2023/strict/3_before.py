def count(words: list[str]) -> list[int]:
    return [len(word) for word in words]


def main() -> None:
    words = ["apple", "banana", "cherry"]
    result = count(words)
    print(result)


if __name__ == "__main__":
    main()

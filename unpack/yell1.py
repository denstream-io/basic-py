# Passes a list


def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased) # unpaCking use case


if __name__ == "__main__":
    main()

def get_priority(char: str) -> int:
    code = ord(char)
    if 97 <= code <= 122:
        return code - 96
    elif 65 <= code <= 90:
        return code - 38
    else:
        return 0


def clear_line(line: str) -> str:
    return line.replace("\n", "")


def get_common_char_priority(line: str) -> int:
    for char in line[(len(line) // 2):]:
        if char in line[:(len(line) // 2)]:
            return get_priority(char)


def count_priorities():
    count = 0
    with open("input.txt") as file:
        for line in file.readlines():
            count += get_common_char_priority(clear_line(line))
    return count


if __name__ == "__main__":
    print(count_priorities())
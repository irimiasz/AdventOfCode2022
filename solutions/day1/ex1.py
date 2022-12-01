def is_line_valid(line: str) -> bool:
    return bool(line.replace("\n", ""))


def get_most_calories() -> int:
    biggest = 0
    cur = 0
    with open("calories.txt") as file:
        for line in file.readlines():
            if is_line_valid(line):
                cur += int(line)
            else:
                if cur > biggest:
                    biggest = cur
                cur = 0
    return biggest


if __name__ == "__main__":
    print(get_most_calories())

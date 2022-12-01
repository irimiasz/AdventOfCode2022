from copy import deepcopy


def is_line_valid(line: str) -> bool:
    return bool(line.replace("\n", ""))


def evaluate_top(top: list[int], cur: int):
    top = deepcopy(top)
    max_index = len(top) - 1
    if cur <= top[max_index]:
        return top
    for index in range(0, max_index):
        if cur >= top[index]:
            for i in range(index, max_index):
                top[index + 1] = top[index]
            top[index] = cur
            break
    return top


def get_top_calories(size: int) -> int:
    top = [0] * size
    cur = 0
    with open("calories.txt", "r") as file:
        for line in file.readlines():
            if is_line_valid(line):
                cur += int(line)
            else:
                top = evaluate_top(top, cur)
                cur = 0

    return sum(top)


if __name__ == "__main__":
    print(get_top_calories(3))

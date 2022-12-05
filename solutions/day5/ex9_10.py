CRATE_COUNT = 9


def parse_input(file) -> tuple[list[list], list[tuple]]:
    columns = [[] for _ in range(CRATE_COUNT)]
    moves = []
    for line in file.readlines():
        if line[0] == "[":
            for i in range(1, len(line), 4):
                if line[i] != " ":
                    columns[i // 4].insert(0, line[i])
        if line[0] == "m":
            moves.append(tuple([int(value) for value in line.split(" ")[1::2]]))
    return columns, moves


def ex9() -> str:
    with open("input.txt", "r") as file:
        columns, moves = parse_input(file)
        for move in moves:
            columns[move[2] - 1] += columns[move[1] - 1][::-1][: move[0]]
            columns[move[1] - 1] = columns[move[1] - 1][: -move[0]]
    return "".join([l[-1] for l in columns])


def ex10() -> str:
    with open("input.txt", "r") as file:
        columns, moves = parse_input(file)
        for move in moves:
            columns[move[2] - 1] += columns[move[1] - 1][-move[0] :]
            columns[move[1] - 1] = columns[move[1] - 1][: -move[0]]
    return "".join([l[-1] for l in columns])


if __name__ == "__main__":
    print(ex9())
    print(ex10())

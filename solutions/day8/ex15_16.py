from math import prod

# another ugly speedrun ;(


def traverse_horizontally(
    height: int,
    w_begin: int,
    w_end: int,
    w_step: int,
    tab: list[list[int]],
    visibles: list[list[bool]],
) -> list[list[bool]]:
    visibles = visibles.copy()
    for i in range(0, height):
        cur = -1
        for j in range(w_begin, w_end, w_step):
            if tab[i][j] > cur:
                visibles[i][j] = True
                cur = tab[i][j]
    return visibles


def traverse_vertically(
    h_begin: int,
    h_end: int,
    h_step: int,
    width: int,
    tab: list[list[int]],
    visibles: list[list[bool]],
) -> list[list[bool]]:
    for i in range(0, width):
        cur = -1
        for j in range(h_begin, h_end, h_step):
            if tab[j][i] > cur:
                visibles[j][i] = True
                cur = tab[j][i]
    return visibles


def get_input_table() -> list[list[int]]:
    tab: list[list[int]] = []
    with open("input.txt") as file:
        for line in file.readlines():
            tab.append([int(c) for c in line.replace("\n", "")])
    return tab


def traverse_vs(tab: [list[list[int]]]) -> list[list[bool]]:
    height = len(tab)
    width = len(tab[0])
    vs = [[False for _ in range(width)] for _ in range(height)]
    return traverse_vertically(
        height - 1,
        -1,
        -1,
        width,
        tab,
        traverse_vertically(
            0,
            height,
            1,
            width,
            tab,
            traverse_horizontally(
                height,
                width - 1,
                -1,
                -1,
                tab,
                traverse_horizontally(height, 0, width, 1, tab, vs),
            ),
        ),
    )


def ex_15() -> int:
    vs = traverse_vs(get_input_table())
    return sum([sum(arr) for arr in vs])


def calculate_scenic_score(i: int, j: int, tab: list[list[int]]):
    size = len(tab)
    scores = [0, 0, 0, 0]
    for k in range(j - 1, -1, -1):
        scores[0] += 1
        if tab[i][k] >= tab[i][j]:
            break
    for k in range(j + 1, size):
        scores[1] += 1
        if tab[i][k] >= tab[i][j]:
            break
    for k in range(i + 1, size):
        scores[2] += 1
        if tab[k][j] >= tab[i][j]:
            break
    for k in range(i - 1, -1, -1):
        scores[3] += 1
        if tab[k][j] >= tab[i][j]:
            break
    return prod([score for score in scores if score > 0])


def ex_16() -> int:
    input = get_input_table()
    vs = traverse_vs(get_input_table())
    height = len(input)
    width = len(input[0])
    sc_max = 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if vs[i][j]:
                sc = calculate_scenic_score(i, j, input)
                if sc > sc_max:
                    sc_max = sc
    return sc_max


if __name__ == "__main__":
    print(ex_15())
    print(ex_16())

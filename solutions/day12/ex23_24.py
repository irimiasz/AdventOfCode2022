from dataclasses import dataclass

MAX_INT = 999999
MAX_ORD = ord("z") + 1
MIN_ORD = ord("a")


@dataclass
class QPoint:
    x: int
    y: int
    val: int | str
    dist: int

    def __repr__(self):
        return f"{self.x}-{self.y}, dist {self.dist}"


def transform(letter):
    if letter == "S":
        return MAX_INT
    if letter == "E":
        return MAX_ORD
    if not letter.isupper():
        return ord(letter)


def get_matrix() -> list[list]:
    with open("input.txt") as file:
        return [
            [transform(el) for el in line.replace("\n", "")]
            for line in file.readlines()
        ]


def get_discovered_matirx(size_x, size_y: int):
    return [[False for _ in range(size_x)] for _ in range(size_y)]


def find_starting_point(matrix: list[list]) -> tuple[int, int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == MAX_INT:
                return i, j


def find_lowest_points(matrix):
    starting_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == MIN_ORD:
                starting_points.append((i, j))
    return starting_points


def is_valid(
    cur_val: int,
    dest_x: int,
    dest_y: int,
    matrix: list[list],
    visited: [list[list[bool]]],
):
    return (
        0 <= dest_x < len(matrix)
        and 0 <= dest_y < len(matrix[0])
        and visited[dest_x][dest_y] is False
        and matrix[dest_x][dest_y] - cur_val <= 1
    )


def shortest_path(matrix: [list[list]], starting_point: tuple[int, int]) -> int:
    discovered = get_discovered_matirx(len(matrix[0]), len(matrix))
    a, b = starting_point
    discovered[a][b] = True
    q = [QPoint(a, b, matrix[a][b], 0)]
    while len(q) > 0:
        q_start = q.pop(0)
        if matrix[q_start.x][q_start.y] == MAX_ORD:
            return q_start.dist - 2
        if is_valid(
            q_start.val, x := q_start.x + 1, y := q_start.y, matrix, discovered
        ):
            q.append(QPoint(x, y, matrix[x][y], q_start.dist + 1))
            discovered[x][y] = True
        if is_valid(
            q_start.val, x := q_start.x - 1, y := q_start.y, matrix, discovered
        ):
            q.append(QPoint(x, y, matrix[x][y], q_start.dist + 1))
            discovered[x][y] = True
        if is_valid(
            q_start.val, x := q_start.x, y := q_start.y + 1, matrix, discovered
        ):
            q.append(QPoint(x, y, matrix[x][y], q_start.dist + 1))
            discovered[x][y] = True
        if is_valid(
            q_start.val, x := q_start.x, y := q_start.y - 1, matrix, discovered
        ):
            q.append(QPoint(x, y, matrix[x][y], q_start.dist + 1))
            discovered[x][y] = True

    return -1


def shortest_path_for_lowest_points(matrix) -> int:
    lowest = MAX_INT
    start_points = find_lowest_points(matrix)
    for start_point in start_points:
        path = shortest_path(matrix, start_point)
        if 0 < ypath < lowest:
            lowest = path
    return lowest


def solutions():
    matrix = get_matrix()
    print(shortest_path(matrix, find_starting_point(matrix)))
    print(shortest_path_for_lowest_points(matrix))


if __name__ == "__main__":
    solutions()

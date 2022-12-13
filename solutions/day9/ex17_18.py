def signum(num: int) -> int:
    if num > 0:
        return 1
    if num == 0:
        return 0
    if num < 0:
        return -1


class Coordinate(list):
    def __add__(self, other):
        if len(self) != len(other):
            raise Exception("Cannot be different sizes")
        return Coordinate([sum(lst) for lst in zip(self, other)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise Exception("Cannot be different sizes")
        return Coordinate([lst[0] - lst[1] for lst in zip(self, other)])

    def is_close(self, other) -> bool:
        return all(
            d <= 1 for d in [abs(coord[0] - coord[1]) for coord in zip(self, other)]
        )

    def move(self, direction: str):
        return self.__add__(DIRECTIONS[direction])

    def move_by_coord(self, vector: list[int]):
        signed = Coordinate([signum(num) for num in vector])
        return self.__add__(signed)


class Rope:
    def __init__(self, length):
        self.coords = [Coordinate([0, 0]) for _ in range(length)]

    def move(self, direction: str):
        self.coords[0] = self.coords[0].move(direction)
        for i in range(1, len(self.coords), 1):
            if not self.coords[i - 1].is_close(self.coords[i]):
                vector = self.coords[i - 1] - self.coords[i]
                self.coords[i] = self.coords[i].move_by_coord(vector)

    def get_head_coord(self) -> Coordinate:
        return self.coords[0]

    def get_tail_coord(self) -> Coordinate:
        return self.coords[-1]


DIRECTIONS = {
    "U": Coordinate([0, 1]),
    "D": Coordinate([0, -1]),
    "L": Coordinate([-1, 0]),
    "R": Coordinate([1, 0]),
}


def parse_line(line: str) -> tuple[str, int]:
    line = line.replace("\n", "").split(" ")
    return line[0], int(line[1])


def solution(length: int) -> int:
    with open("input.txt", "r") as file:
        moved = set()
        rope = Rope(length)
        for line in file.readlines():
            direction, length = parse_line(line)
            for _ in range(length):
                rope.move(direction)
                moved.add(tuple(rope.get_tail_coord()))
        return len(moved)


if __name__ == "__main__":
    print(solution(2))
    print(solution(10))

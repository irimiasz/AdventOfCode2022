def parse_input(line: str) -> dict[int, int]:
    data = list(
        map(int, line.replace("\n", "").replace(",", " ").replace("-", " ").split(" "))
    )
    return {data[0]: data[1], data[2]: data[3]}


def solution() -> tuple[int, int]:
    fully_covered = 0
    partially_covered = 0
    with open("input.txt", "r") as input_file:
        for line in input_file.readlines():
            coverage = parse_input(line)
            if min(coverage.values()) >= max(coverage.keys()):
                partially_covered += 1
            if coverage[max(coverage.keys())] <= coverage[min(coverage.keys())]:
                fully_covered += 1
    return fully_covered, partially_covered


if __name__ == "__main__":
    print(solution())

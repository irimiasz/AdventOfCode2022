from __future__ import annotations
from dataclasses import dataclass

# quite ugly solution, written in a hurry though


@dataclass
class Directory:
    name: str
    size: int = 0
    parent: Directory | None = None

    def __eq__(self, other):
        self.name = other.name

    def __hash__(self):
        return self.name

    def __str__(self):
        return self.name


def parse_name(line: str) -> str:
    return line.replace("\n", "").split(" ")[1]


def parse_size(line: str) -> int:
    return int(line.replace("\n", "").split(" ")[0])


def get_dir_from_entry(dir_map: dict, line: str, cur: Directory) -> Directory:
    entry = line.replace("\n", "").split(" ")[2]
    key = f"{entry}-{cur.name if entry != '/' else ''}"
    return dir_map[key] if entry != ".." else cur.parent


def parse_input() -> dict[str, Directory]:
    dir_map: dict[str, Directory] = {}
    root = Directory(name="/", parent=None)
    dir_map["/-"] = root
    cur = root
    with open("input.txt", "r") as file:
        for line in file.readlines():
            if line.startswith("dir"):
                name = parse_name(line)
                d = Directory(name, 0, cur)
                dir_map[f"{name}-{cur.name}"] = d
            elif line[0].isdigit():
                el = cur
                size = parse_size(line)
                while el is not None:
                    el.size += size
                    el = el.parent
            elif line.startswith("$ cd"):
                d = get_dir_from_entry(dir_map, line, cur)
                cur = d
    return dir_map


def get_sizes(dir_map: dict) -> int:
    return sum([el.size for el in dir_map.values() if el.size <= 100000])


def get_smallest(dir_map: dict) -> int:
    total = 70000000
    need_free = 30000000
    limit = need_free - (total - dir_map["/-"].size)
    return min([el.size for el in dir_map.values() if el.size >= limit])


def main():
    data = parse_input()
    print(get_sizes(data))
    print(get_smallest(data))


if __name__ == "__main__":
    main()

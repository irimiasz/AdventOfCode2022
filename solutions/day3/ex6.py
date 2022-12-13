ASCII_RANGES = [i for i in range(65, 91)] + [i for i in range(97, 123)]

LETTERS = [chr(ascii_code) for ascii_code in ASCII_RANGES]

LETTER_MAP = {k: [False, False, False] for k in LETTERS}


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


def calculate_priority():
    with open("input.txt", "r") as input_file:
        cnt = 0
        priority_sum = 0
        for line in input_file.readlines():
            cnt += 1
            for c in clear_line(line):
                LETTER_MAP[c][cnt % 3 - 1] = True
            if cnt % 3 == 0:
                for k, v in LETTER_MAP.items():
                    if False not in v:
                        priority_sum += get_priority(k)
                    LETTER_MAP[k] = [False, False, False]
        return priority_sum


if __name__ == "__main__":
    print(calculate_priority())

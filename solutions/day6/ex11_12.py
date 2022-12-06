def check_for_duplicates(cnt_val: int) -> int:
    with open("input.txt") as input_file:
        line = input_file.readline()
        cnt = 0
        recent = []
        for char in line:
            cnt += 1
            if cnt <= cnt_val:
                recent.append(char)
            else:
                recent = recent[1:] + [char]
                if len(recent) == len(set(recent)):
                    return cnt


if __name__ == "__main__":
    print(check_for_duplicates(4))
    print(check_for_duplicates(14))

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSS = 0
DRAW = 3

MOVES = {"A": ROCK, "B": PAPER, "C": SCISSORS}

STRATEGY = {"X": LOSS, "Y": DRAW, "Z": WIN}

GAME_SCORE = {
    ROCK: {WIN: PAPER, LOSS: SCISSORS},
    PAPER: {LOSS: ROCK, WIN: SCISSORS},
    SCISSORS: {LOSS: PAPER, WIN: ROCK},
}


def get_data(line: str) -> tuple[int, int]:
    line = line.replace("\n", "")
    return MOVES[line[0]], STRATEGY[line[2]]


def count_points() -> int:
    score = 0
    with open("input.txt") as input_file:
        for line in input_file.readlines():
            opp_move, strategy = get_data(line)
            score += strategy
            if strategy == DRAW:
                score += opp_move
            else:
                score += GAME_SCORE[opp_move][strategy]
    return score


if __name__ == "__main__":
    print(count_points())

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

WIN_POINTS = 6
DRAW_POINTS = 3
LOSS_POINTS = 0

MY_MOVES = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

OPPONENT_MOVES = {"A": ROCK, "B": PAPER, "C": SCISSORS}

POINTS = {ROCK: 1, PAPER: 2, SCISSORS: 3}

WINNING_COMBINATIONS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}


def get_moves(line: str) -> tuple[str, str]:
    line = line.replace("\n", "")
    return MY_MOVES[line[2]], OPPONENT_MOVES[line[0]]


def count_points() -> int:
    score = 0
    with open("input.txt", "r") as input_file:
        for line in input_file.readlines():
            my_move, opponent_move = get_moves(line)
            if opponent_move == WINNING_COMBINATIONS[my_move]:
                score += WIN_POINTS
            elif opponent_move == my_move:
                score += DRAW_POINTS
            else:
                score += LOSS_POINTS
            score += POINTS[my_move]
    return score


if __name__ == "__main__":
    print(count_points())

def shape_score(mine):
    match mine:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
    raise ValueError(f"Unexpected value for mine {mine}")


def outcome_score(opponent, mine):
    if opponent == "A":
        match mine:
            case "X":
                return 3
            case "Y":
                return 6
            case "Z":
                return 0
    if opponent == "B":
        match mine:
            case "X":
                return 0
            case "Y":
                return 3
            case "Z":
                return 6
    if opponent == "C":
        match mine:
            case "X":
                return 6
            case "Y":
                return 0
            case "Z":
                return 3
    raise ValueError(f"Unexpected value for opponent {opponent} or mine {mine}")


def calculate_part_1_score(filename):
    # Part 1
    total_score = 0
    with open(filename, "r") as file:
        for line in file:
            opponent, mine = line.strip().split(" ")
            total_score += (shape_score(mine) + outcome_score(opponent, mine))
    print(f"Total Score: {total_score}")


def find_play_for_outcome(opponent, outcome):
    if opponent == "A":
        match outcome:
            case "X":
                return "Z"
            case "Y":
                return "X"
            case "Z":
                return "Y"
    if opponent == "B":
        match outcome:
            case "X":
                return "X"
            case "Y":
                return "Y"
            case "Z":
                return "Z"
    if opponent == "C":
        match outcome:
            case "X":
                return "Y"
            case "Y":
                return "Z"
            case "Z":
                return "X"
    raise ValueError(f"Unexpected value for opponent {opponent} or outcome {outcome}")


def calculate_part_2_score(filename):
    total_score = 0
    with open(filename, "r") as file:
        for line in file:
            opponent, outcome = line.strip().split(" ")
            mine = find_play_for_outcome(opponent, outcome)
            total_score += (shape_score(mine) + outcome_score(opponent, mine))
    print(f"Total Score: {total_score}")


calculate_part_2_score("input.txt")

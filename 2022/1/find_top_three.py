def find_top_three():
    input_file = "input.txt"
    lines = []
    with open(input_file, "r") as reader:
        lines = reader.readlines()

    current_total = 0
    all_cals = []
    for line in lines:
        if not line.strip():
            all_cals.append(current_total)
            all_cals = sorted(all_cals, reverse=True)[:3]
            current_total = 0
        else:
            current_total += int(line.strip())

    print(f"Top 3: {all_cals}")
    print(f"Sum: {sum(all_cals)}")


find_top_three()

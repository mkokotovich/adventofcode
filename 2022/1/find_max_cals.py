def find_max_cals():
    input_file = "input.txt"
    lines = []
    with open(input_file, "r") as reader:
        lines = reader.readlines()

    max_total = 0
    current_total = 0
    for line in lines:
        if not line.strip():
            if current_total > max_total:
                max_total = current_total
            current_total = 0
        else:
            current_total += int(line.strip())

    print(f"Max: {max_total}")


find_max_cals()

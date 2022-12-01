def find_max_cals():
    input_file = "input.txt"
    max_total = 0
    current_total = 0

    with open(input_file, "r") as reader:
        for line in reader:
            if not line.strip():
                if current_total > max_total:
                    max_total = current_total
                current_total = 0
            else:
                current_total += int(line.strip())
        # the last elf may not have a new line
        if current_total > max_total:
            max_total = current_total


    print(f"Max: {max_total}")


find_max_cals()

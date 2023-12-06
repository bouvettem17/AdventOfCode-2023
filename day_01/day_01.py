calibration_strings = []

with open("./day_01.txt", "r") as file:
    for line in file:
        calibration_strings.append(line)


calibration_sum_one = 0
for line in calibration_strings:
    first_value = ""
    second_value = ""
    i = 0

    while i < len(line):
        if line[i].isdigit():
            if first_value == "":
                first_value = line[i]
            second_value = line[i]
            i += 1
        else:
            i += 1

    final_value = str(first_value) + str(second_value)
    calibration_sum_one += int(final_value)

print(f"Calibration sum for part 1: {calibration_sum_one}")


calibration_sum_two = 0
for line in calibration_strings:
    first_value = ""
    second_value = ""
    i = 0

    while i < len(line):
        if line[i].isdigit():
            if first_value == "":
                first_value = line[i]
            second_value = line[i]
            i += 1
        elif line[i] == "o":
            substring = line[i : i + 3]
            if substring == "one":
                if first_value == "":
                    first_value = 1
                second_value = 1
                i += 2
            else:
                i += 1
        elif line[i] == "t":
            substring_two = line[i : i + 3]
            substring_three = line[i : i + 5]
            if substring_two == "two":
                if first_value == "":
                    first_value = 2
                second_value = 2
                i += 2
            elif substring_three == "three":
                if first_value == "":
                    first_value = 3
                second_value = 3
                i += 4
            else:
                i += 1
        elif line[i] == "f":
            substring_four = line[i : i + 4]
            substring_five = line[i : i + 4]
            if substring_four == "four":
                if first_value == "":
                    first_value = 4
                second_value = 4
                i += 3
            elif substring_five == "five":
                if first_value == "":
                    first_value = 5
                second_value = 5
                i += 3
            else:
                i += 1
        elif line[i] == "s":
            substring_six = line[i : i + 3]
            substring_seven = line[i : i + 5]
            if substring_six == "six":
                if first_value == "":
                    first_value = 6
                second_value = 6
                i += 2
            elif substring_seven == "seven":
                if first_value == "":
                    first_value = 7
                second_value = 7
                i += 4
            else:
                i += 1
        elif line[i] == "e":
            substring_eight = line[i : i + 5]
            if substring_eight == "eight":
                if first_value == "":
                    first_value = 8
                second_value = 8
                i += 4
            else:
                i += 1
        elif line[i] == "n":
            substring_nine = line[i : i + 4]
            if substring_nine == "nine":
                if first_value == "":
                    first_value = 9
                second_value = 9
                i += 3
            else:
                i += 1
        else:
            i += 1

    final_value = str(first_value) + str(second_value)

    calibration_sum_two += int(final_value)


print(f"Calibration sum for part 2: {calibration_sum_two}")

rucksack = "rucksack_organisation.txt"

def file_open(input_file):
    first_rucksack = []
    second_rucksack = []

    with open(input_file, "r") as file:
        for row in file:
            line_lenght = len(row.strip())
            first_rucksack.append(row[:int(line_lenght / 2)])
            second_rucksack.append(row[int(line_lenght / 2):])
    return first_rucksack, second_rucksack

def array_compare(first_list, second_list):
    comparison_founds = []
    loop_count = 0

    for element in first_list:
        for letter in element:
            if letter in second_list[loop_count]:
                comparison_founds.append(letter)
                break
            else:
                pass
        loop_count += 1
    return comparison_founds



if __name__ == "__main__":
    first, second = file_open(rucksack)
    print(array_compare(first, second))
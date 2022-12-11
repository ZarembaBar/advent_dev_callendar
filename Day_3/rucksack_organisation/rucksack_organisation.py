rucksack = "rucksack_organisation.txt"

def open_file_and_transform_to_array(input_file):
    array_from_input_file = []

    with open(input_file, "r") as file:
        for row in file:
            array_from_input_file.append(row.strip())
    return array_from_input_file

def open_file_and_return_two_arrays(input_file):
    first_part_of_string = []
    second_part_of_string = []

    array_to_split = open_file_and_transform_to_array(input_file)
    for element in array_to_split:
        element_lenght = len(element.strip())
        first_part_of_string.append(element[:int(element_lenght / 2)])
        second_part_of_string.append(element[int(element_lenght / 2):])
    return first_part_of_string, second_part_of_string

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

def sum_of_each_element_priority(elements_list):
    elements_priorities_sum = 0

    for element in elements_list:
        if element >= "a" and element <= "z":
            elements_priorities_sum += ord(element) - 96
        elif element >= "A" and element <= "Z":
            elements_priorities_sum += ord(element) - 38
    return elements_priorities_sum

def open_file_and_compare_all_sets_of_three(input_file):
    
    array_to_split = open_file_and_transform_to_array(input_file)
    new_matrix = []
    while array_to_split != []:
        new_matrix.append(array_to_split[:3])
        array_to_split = array_to_split[3:]
    return new_matrix
        
def compare_set_of_three_strings(matrix):
    comparison_faunds = []
    for element in matrix:
        for letter in element[0]:
            if letter in element[1] and letter in element[2]:
                comparison_faunds.append(letter)
                break
    return comparison_faunds

if __name__ == "__main__":
    first, second = open_file_and_return_two_arrays(rucksack)
    priorities_list = array_compare(first, second)
    matrix_from_sets = open_file_and_compare_all_sets_of_three(rucksack)
    matrix_priorities_list = compare_set_of_three_strings(matrix_from_sets)
    print(f"Priority of individual rucsack elements : {sum_of_each_element_priority(priorities_list)}")
    print(f"Priority of sets of three rucsack elements : {sum_of_each_element_priority(matrix_priorities_list)}")
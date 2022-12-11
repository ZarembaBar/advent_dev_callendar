input_file = "pairs_input.txt"

def open_file(input):   #function is splitting file for two arrays of strings "X-Y", and returns them.

    with open(input) as file:
        first_array_of_ranges = []  
        second_array_of_ranges = []

        for row in file:
            first_pair, second_pair = row.split(",")
            first_array_of_ranges.append(first_pair)
            second_array_of_ranges.append(second_pair)
    return first_array_of_ranges, second_array_of_ranges

def convert_string_arrays_to_matrix_of_numbers(first, second):  #Function is converting arrays for two matrixes where first number
    num_of_cycles = len(first)                                  # is start of range and second is enf of range.
    matrix_of_ranges_1 = []
    matrix_of_ranges_2 = []

    for cycle in range(num_of_cycles):
        start_of_range_1, end_of_range_1 = first[cycle].split("-")
        start_of_range_2, end_of_range_2 = second[cycle].split("-")
        matrix_of_ranges_1.append([int(start_of_range_1), int(end_of_range_1)])
        matrix_of_ranges_2.append([int(start_of_range_2), int(end_of_range_2)])
    return matrix_of_ranges_1, matrix_of_ranges_2

def compare_ranges(first_matrix, second_matrix):    #Function compare first and second matrix, counting all sitautions whet one of ranges
    number_of_cycles = len(first_matrix)            #is included in another.
    count_of_included_ranges = 0

    for cycle in range(number_of_cycles):
        if first_matrix[cycle][0] >= second_matrix[cycle][0] and first_matrix[cycle][1] <= second_matrix[cycle][1]:
            count_of_included_ranges += 1
        elif second_matrix[cycle][0] >= first_matrix[cycle][0] and second_matrix[cycle][1] <= first_matrix[cycle][1]:
            count_of_included_ranges += 1
    return count_of_included_ranges

if __name__ == "__main__":
    first, second = open_file(input_file)
    first_ranges_matrix, second_ranges_matrix = convert_string_arrays_to_matrix_of_numbers(first, second)
    print(f"Number of included ranges: {compare_ranges(first_ranges_matrix, second_ranges_matrix)}")

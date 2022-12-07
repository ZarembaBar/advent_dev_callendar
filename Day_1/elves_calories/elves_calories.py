from audioop import reverse


calories_input_file = "calories_input.txt"


#Function reads outside file and convert it into raw list line by line
def load_data(file_name):
    row_list = []
    
    with open(file_name, "r") as file:
        row_list = file.readlines()
    return row_list

#Function takes data from raw list and count sum of intigers untill there is separator \n
#then from converted list of summed intigers, it finds maximum value
def solve(row_list):
    final_calories_list = []
    sum_of_calories = 0
    for row in row_list:
        if row == "\n":
            final_calories_list.append(sum_of_calories)
            sum_of_calories = 0
        else:
            sum_of_calories += int(row)
    final_calories_list.append(sum_of_calories)
    return final_calories_list

#Function adds three top calory snacks
def sum_of_top_three_elves_calories(final_calories_list):
    final_calories_list.sort(reverse = True)
    sum_of_top_three_snacks = 0
    for position in range(3):
        sum_of_top_three_snacks += final_calories_list[position]
    return sum_of_top_three_snacks


if __name__ == "__main__":
    row_list = load_data(calories_input_file)
    final_calories_list = solve(row_list)
    print(f"Top calories snack: {max(final_calories_list)}")
    print(f"Sum calories of 3 top snacks: {sum_of_top_three_elves_calories(final_calories_list)}")


strategy_list = "game_input.txt"

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
#Function returnes points if second player choosed rock
def rock_win_loose_or_tie(player_one_move):
    if player_one_move in rock : return 3
    elif player_one_move in paper : return 0
    elif player_one_move in scissors : return 6  

#Function returnes points if second player choosed paper
def paper_win_loose_or_tie(player_one_move):
    if player_one_move in rock : return 6
    elif player_one_move in paper : return 3
    elif player_one_move in scissors : return 0

#Function returnes points if second player choosed scissors
def scissors_win_loose_or_tie(player_one_move):
    if player_one_move in rock : return 0
    elif player_one_move in paper : return 6
    elif player_one_move in scissors : return 3

#Function reads given file, changing it into two arrays of chooses of first and second player
def input_read(text_file):
    player_one_moves = []
    player_two_moves = []
    
    with open(text_file, "r") as file:
        for row in file:
            player_one, player_two = row.split(" ")
            player_one_moves.append(player_one)
            player_two_moves.append(player_two.strip())
        return player_one_moves, player_two_moves

#Function is counting how much points second player earned, tracking his choices.
def points_count(first_list, second_list):
    loop_cycles = len(first_list)
    sum_of_points = 0

    for cycle in range(loop_cycles):
        if second_list[cycle] in rock:
            sum_of_points += 1
            sum_of_points += rock_win_loose_or_tie(first_list[cycle])
        elif second_list[cycle] in paper:
            sum_of_points += 2
            sum_of_points += paper_win_loose_or_tie(first_list[cycle])
        elif second_list[cycle] in scissors:
            sum_of_points += 3
            sum_of_points += scissors_win_loose_or_tie(first_list[cycle])
    return sum_of_points

if __name__ == "__main__":
    moves_list_one, moves_list_two = input_read(strategy_list)
    print(points_count(moves_list_one, moves_list_two))
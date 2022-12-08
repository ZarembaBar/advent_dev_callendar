strategy_list = "game_input.txt"

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
#Function counts points if second player choosed rock (first part of excersise)
def rock_win_lose_or_tie(player_one_move):
    if player_one_move in rock : return 3
    elif player_one_move in paper : return 0
    elif player_one_move in scissors : return 6  

#Function counts points if second player choosed paper (first part of excersise)
def paper_win_lose_or_tie(player_one_move):
    if player_one_move in rock : return 6
    elif player_one_move in paper : return 3
    elif player_one_move in scissors : return 0

#Function counts points if second player choosed scissors (first part of excersise)
def scissors_win_lose_or_tie(player_one_move):
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
            sum_of_points += rock_win_lose_or_tie(first_list[cycle])
        elif second_list[cycle] in paper:
            sum_of_points += 2
            sum_of_points += paper_win_lose_or_tie(first_list[cycle])
        elif second_list[cycle] in scissors:
            sum_of_points += 3
            sum_of_points += scissors_win_lose_or_tie(first_list[cycle])
    return sum_of_points

#Function counts points if first player choosed rock (second part of excersise)
def strategy_with_A_move_response(player_two_move, lose, draw, win):
    if player_two_move == lose : return 3  
    elif player_two_move == draw : return 4
    elif player_two_move == win : return 8
#Function counts points if first player choosed paper (second part of excersise)
def strategy_with_B_move_response(player_two_move, lose, draw, win):
    if player_two_move == lose : return 1 
    elif player_two_move == draw : return 5
    elif player_two_move == win : return 9
#Function counts points if first player choosed scissors (second part of excersise)
def strategy_with_C_move_response(player_two_move, lose, draw, win):
    if player_two_move == lose : return 2 
    elif player_two_move == draw : return 6
    elif player_two_move == win : return 7

#Function counts points with use of given strategy to lose, win, or draw in order to XYZ encryption
def lose_draw_win_strategy_play(first_list, second_list):
    lose = "X"
    draw = "Y"
    win = "Z"
    loop_cycles = len(first_list)
    sum_of_points = 0

    for cycle in range(loop_cycles):
        if first_list[cycle] == "A":
            sum_of_points += strategy_with_A_move_response(second_list[cycle], lose, draw, win)
        elif first_list[cycle] == "B":
            sum_of_points += strategy_with_B_move_response(second_list[cycle], lose, draw, win)
        elif first_list[cycle] == "C":
            sum_of_points += strategy_with_C_move_response(second_list[cycle], lose, draw, win)
    return sum_of_points

if __name__ == "__main__":
    moves_list_one, moves_list_two = input_read(strategy_list)
    print(f"Without strategy play: {points_count(moves_list_one, moves_list_two)} points")
    print(f"With use of strategy play: {lose_draw_win_strategy_play(moves_list_one, moves_list_two)} points")
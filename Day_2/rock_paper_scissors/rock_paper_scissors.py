
from turtle import clear


strategy_list = "game_input.txt"

#A = X = ROCK
#B = Y = PAPER
#C = Z = SCISSORS
rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]

def rock_win_loose_or_tie(player_one_move):
    if player_one_move in rock:
        return 3
    elif player_one_move in paper:
        return 0
    elif player_one_move in scissors:
        return 6  

def paper_win_loose_or_tie(player_one_move):
    if player_one_move in rock:
        return 6
    elif player_one_move in paper:
        return 3
    elif player_one_move in scissors:
        return 0

def scissors_win_loose_or_tie(player_one_move):
    if player_one_move in rock:
        return 0
    elif player_one_move in paper:
        return 6
    elif player_one_move in scissors:
        return 3

def input_read(text_file):
    player_one_moves = []
    player_two_moves = []
    
    with open(text_file, "r") as file:
        for row in file:
            player_one, player_two = row.split(" ")
            player_one_moves.append(player_one)
            player_two_moves.append(player_two)
        return player_one_moves, player_two_moves

def points_count(first_list, second_list):
    loop_cycles = len(first_list)
    sum_of_points = 0
    for cycle in range(loop_cycles):
        if "X" in second_list[cycle]:
            sum_of_points += 1
            sum_of_points += rock_win_loose_or_tie(first_list[cycle])
        elif "Y" in second_list[cycle]:
            sum_of_points += 2
            sum_of_points += paper_win_loose_or_tie(first_list[cycle])
        elif "Z" in second_list[cycle]:
            sum_of_points += 3
            sum_of_points += scissors_win_loose_or_tie(first_list[cycle])
    return sum_of_points


if __name__ == "__main__":
    moves_list_one, moves_list_two = input_read(strategy_list)
    print(points_count(moves_list_one, moves_list_two))
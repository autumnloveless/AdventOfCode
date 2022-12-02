%dw 2.0
output application/json

var input_map = {
    "X": "A", // rock
    "Y": "B", // paper
    "Z": "C"  // scissor
}

var shape_score_map = {
    "A": 1, // rock
    "B": 2, // paper
    "C": 3  // scissor
}

var shape_strength_map = {
    "A": "C", // rock beats scissor
    "B": "A", // paper beats rock
    "C": "B"  // scissor beats paper
}

fun challenge(opponent_move, my_move) = 
    if (opponent_move == my_move) 3 // tie
    else if (shape_strength_map[opponent_move] == my_move) 0 // i lose
    else 6 // i win

fun calculate_round(opponent_move, my_move) = 
    challenge(opponent_move, my_move) + shape_score_map[my_move]

fun calculate_round_values(processed_input) = 
    processed_input map calculate_round($[0], input_map[$[1]])

var processed_input = input1 splitBy "\n" map ($ splitBy " ")

---
sum(
    calculate_round_values(processed_input)
)
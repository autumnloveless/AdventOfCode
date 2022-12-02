%dw 2.0
output application/json

var result_score = {
    "X": 0, // lose
    "Y": 3, // tie
    "Z": 6  // win
}

var shape_score_map = {
    "A": 1, // rock
    "B": 2, // paper
    "C": 3  // scissor
}

// map shape to what shape wins against it
var winning_shape_map = {
    "C": "A", // scissor loses to rock
    "A": "B", // rock loses to paper
    "B": "C"  // paper loses to scissor
}
// map shape to what shape loses to it
var losing_shape_map = winning_shape_map mapObject { ($): $$ }

fun determine_move(opponent_move, expected_result) = 
    if (expected_result == "X") losing_shape_map[opponent_move] // lose
    else if (expected_result == "Y") opponent_move // tie
    else winning_shape_map[opponent_move] // i win

fun calculate_round(opponent_move, expected_result) = 
    result_score[expected_result] + 
    shape_score_map[determine_move(opponent_move, expected_result)]

fun calculate_round_values(processed_input) = 
    processed_input map calculate_round($[0], $[1])

var processed_input = input1 splitBy "\n" map ($ splitBy " ")

---
sum(
    calculate_round_values(processed_input)
)
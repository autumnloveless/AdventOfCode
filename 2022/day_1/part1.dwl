%dw 2.0
import * from dw::core::Arrays
output text/plain

fun splitByEmptyLine(payload) = payload splitBy "\n\n"
fun splitNumbers(payload) = payload splitBy "\n" map $ as Number

var goblinIndividualCalories = splitByEmptyLine(payload) map splitNumbers($)
var goblinTotalCalories = goblinIndividualCalories map sum($) orderBy -$
---
goblinTotalCalories[0]  // part 1
++ ", " 
++ sum(slice(goblinTotalCalories, 0, 3)) // part 2
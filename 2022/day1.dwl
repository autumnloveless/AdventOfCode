%dw 2.0
import * from dw::core::Arrays
output text/plain

fun elves(elfList) = elfList splitBy "\n\n"
fun calories(elf) = elf splitBy "\n" map $ as Number

var goblinIndividualCalories = elves(payload) map calories($)
var goblinTotalCalories = goblinIndividualCalories map sum($) orderBy -$
---
goblinTotalCalories[0]  // part 1
++ ", " 
++ sum(goblinTotalCalories[0 to 2]) // part 2
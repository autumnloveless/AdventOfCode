%dw 2.0
output application/json
import * from dw::core::Arrays

var processed_input = input1 splitBy "\r\n"

fun string_to_map(str) = str reduce ((char, obj={}) -> obj ++ { (char): sizeOf(obj)+1 })

var character_values = string_to_map("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

fun split_string(str) = str splitBy "" splitAt sizeOf(str)/2

fun get_shared_item(compartment_1, compartment_2_map) =
    compartment_1 filter ((item, index) -> compartment_2_map[item] != null)

fun get_shared_items(items) = items map do {
    var compartments = split_string($)
    ---
    get_shared_item(compartments["l"], string_to_map(compartments["r"]))[0]
}
---
sum(get_shared_items(processed_input) map character_values[$])
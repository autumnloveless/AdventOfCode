%dw 2.0
output application/json
import * from dw::core::Strings
import * from dw::core::Arrays

var processed_input = input1 splitBy "\r\n"

fun string_to_map(str) = str reduce ((char, obj={}) -> obj ++ { (char): sizeOf(obj)+1 })

var character_values = string_to_map("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

fun split_string(str) = str splitBy "" splitAt sizeOf(str)/2

fun get_shared_item(compartment_1, compartment_2_map, compartment_3_map) =
    compartment_1 filter 
        (compartment_2_map[$] != null) and 
        (compartment_3_map[$] != null)

fun get_shared_items(items) = repeat("0,",sizeOf(items)/3) splitBy "," map do {
    var compartment_1 = processed_input[3*($$)]
    var compartment_2 = processed_input[3*($$) + 1]
    var compartment_3 = processed_input[3*($$) + 2]
    ---
    get_shared_item(compartment_1, string_to_map(compartment_2), string_to_map(compartment_3))[0]

}
---

sum(get_shared_items(processed_input) map character_values[$])


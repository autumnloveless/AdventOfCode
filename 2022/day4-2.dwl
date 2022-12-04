%dw 2.0
output application/json
import * from dw::core::Strings
import * from dw::core::Arrays

var processed_input = (input1 splitBy "\r\n") map 
    ($ splitBy "," map 
        ((range) -> range splitBy("-") 
            map (number) -> (number as Number)
        )
    )


fun list_range(min, max) = repeat("0,", max-min+1) splitBy "," map min+$$

---

processed_input reduce ((item, accumulator=0) -> do {
    var elf1 = list_range(item[0][0], item[0][1])
    var elf2 = list_range(item[1][0], item[1][1])
    
    ---
    if (
            (elf1 some (elf2 contains $)) or
            (elf2 some (elf1 contains $))
        )
        accumulator+1
    else
        accumulator
})
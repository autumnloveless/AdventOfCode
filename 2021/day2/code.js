/* 2021 Day 3 */
const fs = require('fs');
let filename = "./2021/day3/input.txt"
// filename = "./2021/day3/test-input.txt"
let nums = fs.readFileSync(filename, 'utf8').split("\n")

// ------------------- Part 1 -------------------
let gammaBit = 0;
let epsilonBit = 0;
let arrayTotals = []

for(let numRow of nums){
    for(let i=0;i<numRow.length-1;i++){

        let existingCount = arrayTotals[i] || { "zeros": 0, "ones": 0 }
        if(numRow.charAt(i) == "0"){
            existingCount.zeros++
        } else {
            existingCount.ones++
        }
        arrayTotals[i] = existingCount
    }
}

gammaBit = arrayTotals.reduce((total, current) => {
    total += current.zeros > current.ones ? "0" : "1"
    return total
}, "")

epsilonBit = arrayTotals.reduce((total, current) => {
    total += current.zeros < current.ones ? "0" : "1"
    return total
}, "")


let gamma = parseInt(gammaBit, 2)
let epsilon = parseInt(epsilonBit, 2)

console.log("gamma:", gamma, "| epsilon:", epsilon)
console.log("product:", gamma*epsilon)
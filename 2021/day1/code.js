/* 2021 Day 1 */
const fs = require('fs');
let filename = "./2021/day1/input.txt"
// filename = "./2021/day1/test-input.txt"

let depthNums = fs.readFileSync(filename, 'utf8').split("\n").map(num => parseInt(num))

// Part 1
let increases = 0
let prevNum = depthNums[0]
for(let num of depthNums){
    if(num > prevNum) { increases++ }
    prevNum = num
}
console.log("Part 1:", increases)


// Part 2
let windowNums = []
for(let i =0;i<depthNums.length-2;i++){
    let sum = depthNums[i] + depthNums[i+1] + depthNums[i+2]
    windowNums.push(sum)
}

increases = 0
prevNum = windowNums[0]
for(let num of windowNums){
    if(num > prevNum) { increases++ }
    prevNum = num
}
console.log("Part 2:", increases)
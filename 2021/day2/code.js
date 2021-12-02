/* 2021 Day 2 */
const fs = require('fs');
let filename = "./2021/day2/input.txt"
// filename = "./2021/day2/test-input.txt"
let nums = fs.readFileSync(filename, 'utf8').split("\n")

// ------------------- Part 1 -------------------
let forward = 0;
let depth = 0;
for(let movement of nums){
    let [direction, magnitude] = movement.split(" ")
    magnitude = parseInt(magnitude)
    switch(direction){
        case "forward":
            forward += magnitude;
            break;
        case "down":
            depth += magnitude
            break;
        case "up":
            depth -= magnitude
            break;
    }
}
console.log("Part 1: ", "distance:", forward, "\t| depth:", depth, "\t\t| product:", depth * forward)


// ------------------- Part 2 -------------------
forward = 0;
depth = 0;
let aim = 0;
for(let movement of nums){
    let [direction, magnitude] = movement.split(" ")
    magnitude = parseInt(magnitude)
    switch(direction){
        case "forward":
            forward += magnitude;
            depth += aim*magnitude;
            break;
        case "down":
            aim += magnitude
            break;
        case "up":
            aim -= magnitude
            break;
    }
}
console.log("Part 2: ", "distance:", forward, "\t| depth:", depth, "\t| product:", depth * forward)
/*
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

*/

const fs = require('fs');

class CorporatePolicy {
    letter: string;
    min: number;
    max: number;
    password: string;

    constructor(letter: string, min: number, max: number, password: string){
      this.letter = letter;
      this.min = min;
      this.max = max;
      this.password = password;
    }
}

const is_password_valid_1 = ({letter, min, max, password}: CorporatePolicy) => {
  // count occurences of letter in password
  // check range
  const occurences = password.split(letter).length - 1;
  
  return occurences >= min && occurences <= max;
}

const is_password_valid_2 = ({letter, min, max, password}: CorporatePolicy) => {
  // check if letters at index min and max equal the expected letter
  // confirm that only one letter matches
  const letter_1 = password[min-1]
  const letter_2 = password[max-1]
  
  return (letter_1 == letter || letter_2 == letter) && (letter_1 != letter_2);
}


/*** 
 *  Code execution starts here
 *  1. get password data from file 'day2-input.txt'
 *  2. save filedata to array
 *  3. map password data to corporate policy
 *  3. reduce passwords:
 *    a. check is_password_valid
 *    b. add 1 to total if true, otherwise 0
 ***/ 

fs.readFile('./day2-input.txt', 'utf8' , (err: any, file_data: any) => {
  if (err) {
    console.error(err);
    return;
  }

  const password_data = file_data.split('\n').map((password_info: string) => {
    const password_split = password_info.split(' ');
    const [min,max] = password_split[0].split('-')
    const letter = password_split[1].slice(0,-1)
    const password = password_split[2]
    return new CorporatePolicy(letter, Number(min), Number(max), password);
  });

  const valid_password_count_part_1 = password_data.reduce((total:number, password_info: CorporatePolicy) => {
    return is_password_valid_1(password_info) ? total+1 : total
  }, 0)

  const valid_password_count_part_2 = password_data.reduce((total:number, password_info: CorporatePolicy) => {
    return is_password_valid_2(password_info) ? total+1 : total
  }, 0)

  console.log("\n=========================================================")
  console.log("Part 1: valid password count is: ", valid_password_count_part_1)
  console.log("Part 2: valid password count is: ", valid_password_count_part_2)
  console.log("=========================================================\n")

})
const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const cards = input[1].split(" ").map(Number);

cards.sort((a, b) => a - b);

let result = 0;
const highest = cards[n - 1];

for (let i = 0; i < n - 1; i++) {
  result += highest + cards[i];
}

console.log(result);

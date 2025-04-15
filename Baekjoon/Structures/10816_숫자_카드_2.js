const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const cards = input[1].split(" ").map(Number);
const M = Number(input[2]);
const numbers = input[3].split(" ").map(Number);

const cardCnt = {};

for (let i = 0; i < N; i++) {
  cardCnt[cards[i]] = (cardCnt[cards[i]] || 0) + 1;
}

const result = [];

for (let j = 0; j < M; j++) {
  result.push(cardCnt[numbers[j]] || 0);
}

console.log(result.join(" "));

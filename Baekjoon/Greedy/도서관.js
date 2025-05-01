const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const books = input[1].split(" ").map(Number);

const negatives = books.filter((x) => x < 0).sort((a, b) => a - b);
const positives = books.filter((x) => x > 0).sort((a, b) => b - a);

let distances = [];

for (let i = 0; i < negatives.length; i += M) {
  distances.push(Math.abs(negatives[i]));
}

for (let i = 0; i < positives.length; i += M) {
  distances.push(positives[i]);
}

const max = Math.max(Math.abs(negatives[0] || 0), Math.abs(positives[0] || 0));

const total = distances.reduce((acc, d) => acc + d * 2, 0) - max;

console.log(total);

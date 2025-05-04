const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const sequence = input[1].split(" ").map(Number);
const numberCount = new Map();

let left = 0;

numberCount.set(sequence[left], 1);

let result = 1;

for (let right = 1; right < N; right++) {
  const rightNum = sequence[right];
  numberCount.set(rightNum, (numberCount.get(rightNum) || 0) + 1);

  while (numberCount.get(rightNum) > M) {
    const leftNum = sequence[left++];
    numberCount.set(leftNum, numberCount.get(leftNum) - 1);
  }

  result = Math.max(result, right - left + 1);
}

console.log(result);

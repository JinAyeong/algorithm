const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const sequence = input[1].split(" ").map(Number);
const numberCount = {};

let left = 0,
  right = 1;

numberCount[sequence[left]] = 1;

let result = 1;

while (left < N && right < N) {
  rightNum = sequence[right];

  if (numberCount[rightNum]) {
    numberCount[rightNum] += 1;
  } else {
    numberCount[rightNum] = 1;
  }

  while (numberCount[rightNum] > M) {
    leftNum = sequence[left++];

    numberCount[leftNum] -= 1;
  }

  const curLength = right - left + 1;

  result = Math.max(curLength, result);

  right += 1;
}

console.log(result);

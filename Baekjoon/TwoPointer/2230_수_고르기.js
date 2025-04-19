const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = [];

for (let i = 0; i < N; i++) {
  arr.push(Number(input[i + 1]));
}

arr.sort((a, b) => a - b);

let result = Number(Infinity);
let left = 0;
let right = 1;

while (left < N) {
  if (arr[right] - arr[left] >= M) {
    result = Math.min(arr[right] - arr[left], result);
    left += 1;
  } else {
    right += 1;
    if (right >= N) {
      break;
    }
  }
}

console.log(result);

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);
let result = Infinity;

for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    const snowman1 = arr[i] + arr[j];

    let left = 0,
      right = N - 1;

    while (left < right) {
      if (left === i || left === j) {
        left += 1;
        continue;
      } else if (right === i || right === j) {
        right -= 1;
        continue;
      }

      const snowman2 = arr[left] + arr[right];

      result = Math.min(Math.abs(snowman2 - snowman1), result);

      if (snowman2 < snowman1) {
        left += 1;
      } else if (snowman1 < snowman2) {
        right -= 1;
      } else {
        break;
      }
    }
  }
}

console.log(result);

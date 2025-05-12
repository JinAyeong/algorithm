const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);

let result = Infinity;
let resultArr = [];

for (let i = 0; i < N - 2; i++) {
  let left = i + 1;
  let right = N - 1;

  while (left < right) {
    const sum = arr[i] + arr[left] + arr[right];

    if (Math.abs(sum) < Math.abs(result)) {
      result = sum;
      resultArr = [arr[i], arr[left], arr[right]];
    }

    if (sum < 0) {
      left++;
    } else {
      right--;
    }
  }
}

console.log(resultArr.join(" "));

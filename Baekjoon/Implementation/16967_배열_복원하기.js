const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [H, W, X, Y] = input[0].split(" ").map(Number); // (H+X) * (W+Y)
const B = input.slice(1, H + 1).map((line) => line.split(" ").map(Number));
const A = Array.from({ length: H }, () => Array(W).fill(0));

for (let i = 0; i < H; i++) {
  for (let j = 0; j < W; j++) {
    if (i >= X && j >= Y) {
      A[i][j] = B[i][j] - A[i - X][j - Y];
    } else {
      A[i][j] = B[i][j];
    }
  }
}

A.forEach((row) => console.log(row.join(" ")));

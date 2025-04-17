const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let line = 0;
const tc = Number(input[line++]);

for (let t = 0; t < tc; t++) {
  const [L, N] = input[line++].split(" ").map(Number);
  const location = [];

  for (let i = 0; i < N; i++) {
    location.push(Number(input[line++]));
  }

  location.sort((a, b) => a - b);

  let max_time = 0;
  let min_time = 0;

  for (const l of location) {
    max_time = Math.max(max_time, l, L - l);
    min_time = Math.max(min_time, Math.min(l, L - l));
  }

  console.log(min_time, max_time);
}

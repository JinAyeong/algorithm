const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const titles = [];

for (let i = 1; i <= N; i++) {
  const [name, power] = input[i].split(" ");
  titles.push([name, Number(power)]);
}

const result = [];

for (let i = N + 1; i < N + 1 + M; i++) {
  const num = Number(input[i]);

  let left = 0;
  let right = N - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midPower = titles[mid][1];

    if (midPower < num) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  result.push(titles[left][0]);
}

console.log(result.join("\n"));

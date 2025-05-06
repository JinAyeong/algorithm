const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const pos = [];

let cur = input[1].split(" ").map(Number);
pos.push(cur);

let totalDist = 0;

// 총 거리 및 위치 구하기
for (let i = 2; i < N + 1; i++) {
  const [x, y] = input[i].split(" ").map(Number);
  pos.push([x, y]);
  totalDist += Math.abs(cur[0] - x) + Math.abs(cur[1] - y);
  cur = [x, y];
}

let result = Number(Infinity);

// 하나씩 없애보기
for (let j = 1; j < N - 1; j++) {
  const a =
    Math.abs(pos[j - 1][0] - pos[j][0]) + Math.abs(pos[j - 1][1] - pos[j][1]);
  const b =
    Math.abs(pos[j + 1][0] - pos[j][0]) + Math.abs(pos[j + 1][1] - pos[j][1]);
  const c =
    Math.abs(pos[j + 1][0] - pos[j - 1][0]) +
    Math.abs(pos[j + 1][1] - pos[j - 1][1]);

  const newDist = totalDist - (a + b) + c;

  result = Math.min(result, newDist);
}

console.log(result);

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input.slice(1, N + 1).map((line) => line.split(" ").map(Number));
let min_sum = Number(Infinity);

const dfs = (i, A_team, B_team, A_sum, B_sum) => {
  if (A_team.length === N / 2 && B_team.length === N / 2) {
    min_sum = Math.min(min_sum, Math.abs(A_sum - B_sum));
    return;
  }

  // A 팀에 합류
  if (A_team.length < N / 2) {
    let A_next = A_sum;
    for (const a of A_team) {
      A_next += arr[a][i] + arr[i][a];
    }
    dfs(i + 1, [...A_team, i], B_team, A_next, B_sum);
  }

  // B 팀에 합류
  if (B_team.length < N / 2) {
    let B_next = B_sum;
    for (const b of B_team) {
      B_next += arr[b][i] + arr[i][b];
    }
    dfs(i + 1, A_team, [...B_team, i], A_sum, B_next);
  }
};

dfs(0, [], [], 0, 0);

console.log(min_sum);

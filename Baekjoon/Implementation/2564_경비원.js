const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const C = Number(input[1]);
const stores = input.slice(2, 2 + C).map((line) => line.split(" ").map(Number));
const [dongeunDir, dongeunDist] = input[2 + C].split(" ").map(Number);

const perimeter = 2 * (N + M); // 외곽 둘레

// 위치 -> 외곽 거리 기준 환산
const getPosition = ([dir, dist]) => {
  switch (dir) {
    case 1: // 북
      return dist;
    case 2: // 남
      return N + M + (N - dist);
    case 3: // 서
      return 2 * (N + M) - dist;
    case 4: // 동
      return N + dist;
  }
};

const guardPos = getPosition([dongeunDir, dongeunDist]);

let result = 0;

for (const store of stores) {
  const storePos = getPosition(store);
  const direct = Math.abs(guardPos - storePos);
  result += Math.min(direct, perimeter - direct);
}

console.log(result);

input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [[M, N], ...mp] = input.map((row) => row.split(" ").map(Number));

let queue = [];
let day = 0;

// 초기의 익은 토마토
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (mp[i][j] === 1) {
      queue.push([i, j]);
    }
  }
}

// 토마토 익히기
while (queue.length > 0) {
  const nextQueue = [];

  queue.forEach(([x, y]) => {
    [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
    ].forEach(([dx, dy]) => {
      const nx = x + dx,
        ny = y + dy;
      if (0 <= nx && nx < N && 0 <= ny && ny < M && mp[nx][ny] === 0) {
        nextQueue.push([nx, ny]);
        mp[nx][ny] = 1;
      }
    });
  });

  queue = nextQueue;
  if (queue.length > 0) {
    day++;
  }
}

// 모든 토마토가 익었는지 확인
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (mp[i][j] === 0) {
      day = -1;
      break;
    }
  }
  if (day === -1) {
    break;
  }
}

console.log(day);
